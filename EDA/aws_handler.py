import boto3

class AwsDataHandler():
    """
    To upload/download data from aws s3
    :param aws_file_path: Path in AWS S3 where the file should be stored or retrieved from.
    :param file_path: Local file path (optional, required for upload).
    """
    def __init__(self, aws_file_path:str, file_path:str=None):
        self.file_path = file_path
        self.aws_file_path = aws_file_path
        self.bucket_name = 'aws-s3-data-for-projects'

    def save_data_to_aws(self):
        """
        Upload the file to aws s3
        """
        if not self.file_path:
            raise ValueError('file_path is not file to upload the data')

        try:
            s3 = boto3.client('s3')
        except Exception as e:
            print(f'Error while connecting to AWS s3: {e}')
            raise ConnectionError('did not connect to aws')
        if s3:
            s3.upload_file(self.file_path, self.bucket_name, self.aws_file_path)
            print("SAVED")
        else:
            raise FileNotFoundError('give correct path')

    def get_data_from_aws(self):
        """
        Returns a file url which can be used to read files  ---  req. s3fs - pip install s3fs
        """
        try:
            s3_url = f's3://{self.bucket_name}/{self.aws_file_path}'
            print('connecting to: ', s3_url)
        except Exception as e:
            print(e)
        return s3_url


# if __name__ == '__main__':
    # import pandas as pd
    # file_path='data/aircraft engine/PM_train.parquet'
    # aws_file_path='data/predictive-maintenance/clean_data/clean_data.parquet'
    # downloader = AwsDataHandler(aws_file_path=aws_file_path)
    # path = downloader.get_data_from_aws()
    # df = pd.read_parquet(path)
    # df.info()
