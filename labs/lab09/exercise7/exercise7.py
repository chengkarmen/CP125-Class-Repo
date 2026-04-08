import pandas as pd


def promotion_candidates(filename):
    data = pd.read_csv(filename)
    average_performance = data['PerformanceScore'].mean()
    min_years_required = 2
    candidate_count = len(data.loc[(data['YearsOfService'] > min_years_required) & (data['PerformanceScore'] > average_performance)])
    candidate_names = set(data.loc[(data['YearsOfService'] > min_years_required) & (data['PerformanceScore'] > average_performance), 'EmployeeName'])
    return {'average_performance': average_performance,
            'min_years_required': min_years_required,
            'candidate_count': candidate_count,
            'candidate_names': candidate_names}
