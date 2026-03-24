#dataset overview
def dataset_overview(df):
    print("Dataset Shape:", df.shape)
    print("\nColumn Information:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    
#class_distribution
def class_distribution(df):
    print("\nClass Distribution:")
    print(df['label'].value_counts())
    
#attack_category_distribution
def attack_category_distribution(df):
    df['label'] = df['label'].str.replace('.', '', regex=False)
    
    attack_map = {
        'normal': 'Normal',
        'back': 'DoS', 'land': 'DoS', 'neptune': 'DoS',
        'pod': 'DoS', 'smurf': 'DoS', 'teardrop': 'DoS',
        'ipsweep': 'Probe', 'nmap': 'Probe',
        'portsweep': 'Probe', 'satan': 'Probe',
        'ftp_write': 'R2L', 'guess_passwd': 'R2L',
        'imap': 'R2L', 'multihop': 'R2L',
        'phf': 'R2L', 'spy': 'R2L',
        'warezclient': 'R2L', 'warezmaster': 'R2L',
        'buffer_overflow': 'U2R', 'loadmodule': 'U2R',
        'perl': 'U2R', 'rootkit': 'U2R'
    }

    df['attack_type'] = df['label'].map(attack_map)
    print("\nAttack Category Distribution:")
    print(df['attack_type'].value_counts())
    
#protocol_service_analysis
def protocol_service_analysis(df):
    print("\nProtocol Type Distribution:")
    print(df['protocol_type'].value_counts())

    print("\nTop 10 Services:")
    print(df['service'].value_counts().head(10))

#statistical_summary
def statistical_summary(df):
    print("\nStatistical Summary:")
    print(df.describe())
