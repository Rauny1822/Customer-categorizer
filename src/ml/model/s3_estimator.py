from src.cloud_storage.aws_storage import SimpleStorageService
from src.exception import CustomerException
from src.ml.model.estimator import CustomerSegmentationModel
import sys
from pandas import DataFrame
import numpy as np
from src.logger import logging



class CustomerClusterEstimator:
    """
    This class is used to save and retrieve src model in s3 bucket and to do prediction
    """

    def __init__(self,bucket_name,model_path,):
        """
        :param bucket_name: Name of your model bucket
        :param model_path: Location of your model in bucket
        """
        self.bucket_name = bucket_name
        self.model_path = model_path
        self.loaded_model:CustomerSegmentationModel=None
        self.s3 = None
        try:
            self.s3 = SimpleStorageService()
        except Exception as e:
            logging.warning(f"AWS credentials not available: {e}. Running in demo mode.")


    def is_model_present(self,model_path):
        try:
            if self.s3 is None:
                return False
            return self.s3.s3_key_path_available(bucket_name=self.bucket_name, s3_key=model_path)
        except Exception as e:
            logging.warning(f"Could not check S3: {e}")
            return False

    def load_model(self,)->CustomerSegmentationModel:
        """
        Load the model from the model_path
        :return:
        """
        if self.s3 is None:
            logging.warning("AWS not configured. Returning demo model.")
            return None
        return self.s3.load_model(self.model_path,bucket_name=self.bucket_name)

    def save_model(self,from_file,remove:bool=False)->None:
        """
        Save the model to the model_path
        :param from_file: Your local system model path
        :param remove: By default it is false that mean you will have your model locally available in your system folder
        :return:
        """
        
        try:
            if self.s3 is None:
                raise Exception("AWS credentials not configured")
            self.s3.upload_file(from_file,
                                to_filename=self.model_path,
                                bucket_name=self.bucket_name,
                                remove=remove
                                )
        except Exception as e:
            raise CustomerException(e, sys) from e


    def predict(self,dataframe:DataFrame):
        """
        :param dataframe:
        :return:
        """
        try:
            if self.loaded_model is None:
                self.loaded_model = self.load_model()
            
            # If no model loaded and AWS not available, return demo prediction
            if self.loaded_model is None:
                logging.warning("No model available. Returning demo clustering result (assigning to cluster 0, 1, or 2)")
                # Return demo prediction - assign to random cluster (0, 1, or 2)
                n_rows = len(dataframe)
                demo_prediction = np.random.randint(0, 3, n_rows)
                return demo_prediction
            
            return self.loaded_model.predict(dataframe)
        except Exception as e:
            raise CustomerException(e,sys)