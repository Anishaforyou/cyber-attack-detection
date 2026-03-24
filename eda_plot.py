import matplotlib.pyplot as plt
import seaborn as sns

def plot_label_distribution(df):

    df['label'] = df['label'].str.replace('.', '', regex=False)

    plt.figure(figsize=(10,6))
    df['label'].value_counts().head(10).plot(kind='bar')

    plt.title("Top Attack Types Distribution")
    plt.xlabel("Attack Type")
    plt.ylabel("Count")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
def plot_protocol_distribution(df):
    """Protocol Type Distribution"""

    plt.figure(figsize=(6,4))
    sns.countplot(x='protocol_type', data=df)

    plt.title("Protocol Type Distribution")
    plt.xlabel("Protocol Type")
    plt.ylabel("Count")

    plt.show()

def plot_top_services(df):

    top_services = df['service'].value_counts().head(10)

    plt.figure(figsize=(10,5))
    sns.barplot(x=top_services.index, y=top_services.values)

    plt.title("Top 10 Network Services")
    plt.xlabel("Service")
    plt.ylabel("Count")

    plt.xticks(rotation=45)
    plt.show()
    
def plot_flag_distribution(df):

    plt.figure(figsize=(8,5))
    sns.countplot(x='flag', data=df)

    plt.title("Connection Flag Distribution")
    plt.xlabel("Flag")
    plt.ylabel("Count")

    plt.show()
    
def plot_src_bytes_distribution(df):

    plt.figure(figsize=(8,5))

    sns.histplot(df['src_bytes'], bins=50)

    plt.title("Source Bytes Distribution")
    plt.xlabel("Source Bytes")
    plt.ylabel("Frequency")

    plt.show()

def plot_correlation_heatmap(df):

    numeric_df = df.select_dtypes(include=['int64','float64'])

    plt.figure(figsize=(12,10))

    sns.heatmap(numeric_df.corr(),
                cmap='coolwarm',
                linewidths=0.5)

    plt.title("Feature Correlation Heatmap")

    plt.show()

