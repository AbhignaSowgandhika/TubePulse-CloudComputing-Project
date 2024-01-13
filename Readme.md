# <a name="_khu82qlpyqzn"></a>**TubePulse: Harnessing Youtube Insights Using The Cloud**
This project aims to securely manage, streamline, and perform analysis on the structured and semi-structured YouTube videos data based on the video categories and the trending metrics.
## <a name="_mfymi4aqp582"></a>**Overview**
This is a comprehensive exploration into the vast realm of Youtube data, aiming to uncover insights into popular topics, user engagement, sentiment trends in comments. Leveraging the robust Youtube Data and an array of cutting-edge tools such as AWS Glue, Lambda, Athena, and QuickSight our project delves into data collection, processing, and sophisticated analysis.

## <a name="_vfoa18qfshjp"></a>**Architecture**

The main components are:

- Data Storage - Store the data into 3 S3 Buckets - Raw, Cleansed and Analytics
- Processing - ETL Job and Lambda functions to process & transform JSON, CSV data into Apache Parquet format
- Joining - Joining the cleansed data using AWS Athena Queries and ETL Job
- Metadata - AWS Glue crawlers to catalog dataset schema
- Analysis - Using AWS QuickSight
## <a name="_xc2hso25b26u"></a>**Implementation Details**
Key steps:

- Configure S3 buckets
- Develop ETL logic in Python
- Deploy Glue ETL Job for CSV to Parquet Conversion
- Deploy AWS Lambda Function for JSON to Parquet Conversion
- Data Joining using ETL Job
- Dashboards creation using QuickSight
## <a name="_9918s34u70he"></a>**Getting Started**
Prerequisites:

- AWS environment with access keys
- Python, AWS CLI/SDK
## <a name="_1psm2npov8a1"></a>**Next Steps**
Future enhancements:

- EScheduled ETL Jobs
- Enhanced Dashboard Experiences
- Continuous Monitoring and Optimization
- Machine Learning Integration

