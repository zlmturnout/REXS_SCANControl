from PySide6.QtCore import Qt,QMetaObject,Signal,Slot
from PySide6.QtWidgets import QTreeView,QTreeWidget,QTreeWidgetItem,QHBoxLayout,QHeaderView,QWidget
from PySide6.QtGui import QIcon,QAction,QPixmap,QPainter,QColor,QFont
from PySide6.QtSql import QSqlDatabase

class SqlTreeWidget(QWidget):
    """
    Customed TreeWidget for SQL databases tableView
    """
    # signals used
    tableActivated_sig=Signal(str)  # emit table name to show data in this table
    requestMetaData_sig=Signal(str) # emit table name to request schema information
    
    def __init__(self,parent=None):
        super(SqlTreeWidget, self).__init__()
        self.layout=QHBoxLayout(self)
        self.tree=QTreeWidget(self)
        self.tree.setObjectName("tree")
        self.tree.setHeaderLabel("SQL Database")
        self.tree.header().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.layout.addWidget(self.tree)
        self.refreshAction=QAction('Refresh',self.tree)
        self.metadataAction=QAction('Show Schema',self.tree)
        self.refreshAction.triggered.connect(self.refresh)
        self.metadataAction.triggered.connect(self.show_metadata)
        self.addAction(self.metadataAction)
        self.addAction(self.refreshAction)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        QMetaObject.connectSlotsByName(self)
        # current database
        self.current_db=''
        self.active_db=''
    
    @staticmethod
    def qDBCaption(database:QSqlDatabase):
        """get the current database caption

        Args:
            database (QSqlDatabase): connected database
        Returns:
            db_caption(str): drivername:[userName@]databaseName
        """
        db_caption=database.driverName()+':'
        if database.userName():
            db_caption+=database.userName()+'@'
        db_caption+=database.databaseName()
        return db_caption
        
    @Slot()
    def refresh(self):
        """ Refresh the tree
        """
        self.tree.clear()
        self.db_active_flag=False
        connection_names=QSqlDatabase.connectionNames()
        for connected_dbname in connection_names:
            root=QTreeWidgetItem(self.tree)
            db=QSqlDatabase.database(connected_dbname,False)
            root.setText(0,self.qDBCaption(db))
            # set active database if found
            if connected_dbname==self.active_db:
                self.db_active_flag=True
                self.set_db_active(root)
            if db.isOpen():
                all_tables=db.tables()
                for table_name in all_tables:
                    table_item=QTreeWidgetItem(root)
                    table_item.setText(0,table_name)
        # set first connected database as active if not found
        if not self.db_active_flag:
            self.active_db=connection_names[0]
            self.set_db_active(self.tree.topLevelItem(0))
        self.tree.doItemsLayout()
    
    @staticmethod
    def setBold(treeItem:QTreeWidgetItem,bold:bool):
        font=treeItem.font(0)
        font.setBold(bold)
        treeItem.setFont(0,font)
    
    def set_db_active(self,item:QTreeWidgetItem):
        """set active database
        """
        for i in range(self.tree.topLevelItemCount()):
            if self.tree.topLevelItem(i).font(0).bold():
                self.setBold(self.tree.topLevelItem(i),False)
        
        # noothing to set
        if not item:
            return 0
        self.setBold(item,True)
        self.active_db=QSqlDatabase.connectionNames()[self.tree.indexOfTopLevelItem(item)]
    
    def currentDatabase(self):
        #print(f'current active database:{self.active_db}')
        self.current_db=QSqlDatabase.database(self.active_db)
        return self.current_db
            
    @Slot(QTreeWidgetItem,int)
    def on_tree_itemActivated(self,item:QTreeWidgetItem,n:int):
        """ tree item activated event process
        emit table item activated signal if get table
        Args:
            item (QTreeWidgetItem): database or table
            n (int): column
        """
        if not item.parent():
            self.set_db_active(item)
        else:
            self.set_db_active(item.parent())
            self.tableActivated_sig.emit(item.text(0))
        
    @Slot() 
    def show_metadata(self):
        """ Show the schema information
        """
        current_item=self.tree.currentItem()
        if not current_item or not current_item.parent():
            return 0
        self.set_db_active(current_item.parent())
        self.requestMetaData_sig.emit(current_item.text(0))
    
    @Slot(QTreeWidgetItem,QTreeWidgetItem)
    def on_tree_currentItemChanged(self,currentItem:QTreeWidgetItem,previousitem:QTreeWidgetItem):
        if currentItem and currentItem.parent():
            self.metadataAction.setEnabled(True)
        else:
            self.metadataAction.setEnabled(False)
