import yaml
import os,sys
sys.path.append('.')

def read_yaml_data(filepath:str):
    """read yaml data from file

    Args:
        filepath (str): absolute path
    """
    with open(filepath,'r',encoding="UTF-8") as f:
        yaml_data=yaml.load(f,Loader=yaml.FullLoader)
    return yaml_data

if __name__=="__main__":
    yaml_file=os.path.abspath('.\\Architect\\PV_names_E20U2.yaml')
    print(yaml_file)
    yaml_data=read_yaml_data(yaml_file)
    print(yaml_data)
    print(yaml_data["BeamLine"]["PGM1_E"]["SE_SET"])