
import numpy as np


def simulate_daily_demand(nDays, averageDemand):
    return np.random.poisson(averageDemand, nDays)

def analyze_results(dailyDemand):  
    meanDemand = np.mean(dailyDemand)
    stdDevDemand = np.std(dailyDemand)
    percentile5 = np.percentile(dailyDemand, 5)
    percentile95 = np.percentile(dailyDemand, 95)
    
    return {
        'mean': meanDemand,
        'std_dev': stdDevDemand,
        '5th_percentile': percentile5,
        '95th_percentile': percentile95
    }

def simulate_monthly_demand(nSimulations, nDays, averageDailyDemand):
    monthlyDemands = []
    for day in range(nSimulations):
        dailyDemand = simulate_daily_demand(nDays, averageDailyDemand)
        monthlyDemands.append(np.sum(dailyDemand))
    
    return np.array(monthlyDemands)

def calculate_optimal_inventory(monthlyDemands, serviceLevel):
    
    return np.percentile(monthlyDemands, serviceLevel * 100)

def main():
    # Create a user interface to input different assumptions (e.g., average daily demand, service level).

    nDays = int(input("For how many days would you like to do the simulation for?\n"))
    averageDailyDemand = int(input("What is the average dayly demand?\n"))  
    
    dailyDemand = simulate_daily_demand(nDays, averageDailyDemand)
    
    results = analyze_results(dailyDemand)
    print("Daily Demand Analysis:")
    for key, value in results.items():
        print(f"{key}: {value}")
    
    nSimulations = int(input("How many simmulations would you like to run? (We reccomend somewhere areound 1000 for better results)\n"))  
    monthlyDemands = simulate_monthly_demand(nSimulations, nDays, averageDailyDemand)
    
    serviceLevel = int(input("What is the percentage of service level would you like to maintain?"))
    serviceLevel = serviceLevel/100
    optimalInventory = calculate_optimal_inventory(monthlyDemands, serviceLevel)
    
    print(f"\nOptimal Inventory Level to meet {serviceLevel*100}% service level: {optimalInventory}")


main()
   