import pandas as pd
import argparse
import joblib
import os
import logging
from src.utils.common_utils import (
    read_params, 
    create_dir, 
    save_reports )
from sklearn.linear_model import ElasticNet

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=logging_str)


def train(config_path):
    config = read_params(config_path)
    artifacts = config['artifacts']
    split_data = artifacts["split_data"]
    train_data_path = split_data["train_path"]
    test_data_path = split_data["test_path"]
    
    base = config["base"]
    random_seed = base["random_state"]
    target = base["target_col"]

    reports = artifacts["reports"]
    reports_dir = reports["reports_dir"]
    params_file = reports["params"]

    ElasticNet_params = config["estimators"]["ElasticNet"]["params"]
    alpha = ElasticNet_params["alpha"]
    l1_ratio = ElasticNet_params["l1_ratio"]

    model_dir = artifacts["model_dir"]
    model_path = os.path.join(model_dir,"model.joblib")

    train = pd.read_csv(train_data_path, sep =",")
    train_y = train[target]
    train_x = train.drop(target, axis =1)

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_seed)
    lr.fit(train_x,train_y)

    create_dir([reports_dir, model_dir])
    

    params = {
        "alpha" : alpha,
        "l1_ratio": l1_ratio
         }
    joblib.dump(lr,model_path)
    logging.info(f"model saved at {model_path}")

    save_reports(params_file,params)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        data = train(config_path=parsed_args.config)
        logging.info("training of the model stage is completed")
    except Exception as e:
        logging.error(e)
        # raise e
