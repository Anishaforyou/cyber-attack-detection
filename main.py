from read import read_dataset
import eda
import eda_plot as ep

#step 1 reading the dataset
df = read_dataset()

 
#step 2 eda 
eda.dataset_overview(df)
eda.class_distribution(df)
eda.attack_category_distribution(df)
eda.protocol_service_analysis(df)
eda.statistical_summary(df)

#step 3 eda_plot
ep.plot_label_distribution(df)
ep.plot_protocol_distribution(df)
ep.plot_top_services(df)
ep.plot_flag_distribution(df)
ep.plot_src_bytes_distribution(df)
ep.plot_correlation_heatmap(df)