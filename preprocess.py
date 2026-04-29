import pandas as pd
from sklearn.preprocessing import StandardScaler

# ------------------------------------------
# Attack Mapping Dictionary
# ------------------------------------------
attack_map = {
    'normal': 'Normal',

    # DoS attacks
    'back': 'DoS', 'land': 'DoS', 'neptune': 'DoS',
    'pod': 'DoS', 'smurf': 'DoS', 'teardrop': 'DoS',

    # Probe attacks
    'ipsweep': 'Probe', 'nmap': 'Probe',
    'portsweep': 'Probe', 'satan': 'Probe',

    # R2L attacks
    'ftp_write': 'R2L', 'guess_passwd': 'R2L',
    'imap': 'R2L', 'multihop': 'R2L',
    'phf': 'R2L', 'spy': 'R2L',
    'warezclient': 'R2L', 'warezmaster': 'R2L',

    # U2R attacks
    'buffer_overflow': 'U2R', 'loadmodule': 'U2R',
    'perl': 'U2R', 'rootkit': 'U2R'
}

# ------------------------------------------
# Step 1: Clean Labels
# ------------------------------------------
def clean_labels(df):
    # Remove '.' from labels like 'normal.'
    df['label'] = df['label'].str.replace('.', '', regex=False)
    return df


# ------------------------------------------
# Step 2: Map Attack Types
# ------------------------------------------
def map_attack_types(df):
    df['attack_type'] = df['label'].map(attack_map)
    return df


# ------------------------------------------
# Step 3: Create Binary Label
# ------------------------------------------
def create_binary_label(df):
    df['binary_label'] = df['attack_type'].apply(
        lambda x: 0 if x == 'Normal' else 1
    )
    return df


# ------------------------------------------
# Step 4: Encode Categorical Features
# ------------------------------------------
def encode_features(df):
    categorical_cols = ['protocol_type', 'service', 'flag']
    df = pd.get_dummies(df, columns=categorical_cols)
    return df


# ------------------------------------------
# Step 5: Split Features and Labels
# ------------------------------------------
def split_features_labels(df):
    X = df.drop(columns=['attack_type', 'binary_label', 'label'])
    y_binary = df['binary_label']
    y_multi = df['attack_type']
    return X, y_binary, y_multi


# ------------------------------------------
# Step 6: Feature Scaling
# ------------------------------------------
def scale_features(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler


# ------------------------------------------
# Main Preprocessing Pipeline
# ------------------------------------------
def preprocess_data(df):
    df = clean_labels(df)
    df = map_attack_types(df)
    df = create_binary_label(df)
    df = encode_features(df)

    X, y_binary, y_multi = split_features_labels(df)
    X_scaled, scaler = scale_features(X)

    return X_scaled, y_binary, y_multi, scaler