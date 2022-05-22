# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
def updated_damages(damage):
    conversion = {"M": 1000000, "B": 1000000000}
    damage_updated = []
    for data in damage:
        if data[-1] in conversion:
            data = float(data[:-1]) * conversion.get(data[-1])
            damage_updated.append(data)
        else:
            damage_updated.append(data)
    return damage_updated


updated_damage = updated_damages(damages)
print(updated_damage)

# write your construct hurricane dictionary function here:
def hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricane_detail = ["Name", "Month", "Year", "Max Sustained Wind", "Areas Affected", "Damage", "Death"]
    hurricane = []
    for index in range(34):
        hurricane.append({"Name": names[index], "Month": months[index], "Year": years[index],
                          "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index],
                          "Damage": damages[index], "Death": deaths[index]})
    zipped_hurricane_names = list(zip(names, hurricane))
    hurricane_names = {key: value for key, value in zipped_hurricane_names}
    return hurricane_names


name = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print(name.get("Cuba I"))


# write your construct hurricane by year dictionary function here:
def hurricane_year_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    # hurricane_detail = ["Name", "Month", "Year", "Max Sustained Wind", "Areas Affected", "Damage", "Death"]
    hurricane = []
    for index in range(34):
        hurricane.append({"Name": names[index], "Month": months[index], "Year": years[index],
                          "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index],
                          "Damage": damages[index], "Death": deaths[index]})
    zipped_hurricane_years = list(zip(years, hurricane))
    hurricane_years = {}
    for key, value in zipped_hurricane_years:
        if key in hurricane_years:
            hurricane_years[key] = hurricane_years[key], value
        else:
            hurricane_years[key] = value
    return hurricane_years


year = hurricane_year_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)
print(year[1932])


# write your count affected areas function here:
def area_count(areas_affect):
    count = 0
    areas_affected_count = {}
    for area in areas_affect:
        for key in area:
            if key in areas_affected_count:
                count += 1
                areas_affected_count[key] = count
            else:
                areas_affected_count[key] = count
    return areas_affected_count


count = area_count(areas_affected)
print(count)


# write your find most affected area function here:
def most_areas_affected(areas_affected):
    counted_area = area_count(areas_affected)
    max_area = {}
    max_counted = max(counted_area.values())
    for key, value in counted_area.items():
        if value == max_counted:
            max_area[key] = value
        elif value in max_area:
            max_area[key] = max_area[key], value
    return max_area


m = most_areas_affected(areas_affected)
print(m)


# write your greatest number of deaths function here:
# write your greatest number of deaths function here:
def most_areas_affected(names, deaths):
    zipped_names_deaths = list(zip(names, deaths))
    max_death = max(deaths)
    max_dict = {}

    for key, value in zipped_names_deaths:
        if value == max_death:
            max_dict[key] = value
    return max_dict


d = most_areas_affected(names, deaths)
print(d)


# write your category by mortality function here:
def hurricane_mortality(deaths):
    # mortality_scale = {0: 0,1: 100, 2: 500, 3: 1000, 4: 10000, 5:>10000}
    mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for death in deaths:
        for key, value in mortality.items():
            if key == 0 and death <= 0:
                key = value.append(death)
            elif key == 1 and 0 < death <= 100:
                key = value.append(death)
            elif key == 2 and 100 < death <= 500:
                key = value.append(death)
            elif key == 3 and 500 < death <= 1000:
                key = value.append(death)
            elif key == 4 and 1000 < death <= 10000:
                key = value.append(death)
            elif key == 5 and death > 10000:
                key = value.append(death)
    return mortality


mortality = hurricane_mortality(deaths)
print(mortality)


# write your greatest damage function here:
# write your greatest damage function here:
def greatest_damages_and_cost(names, damages):
    zipped_names_damages = list(zip(names, damages))

    names_costs = {}
    for key, value in zipped_names_damages:
        if value == "Damages not recorded":
            names_costs[key] = 0
        else:
            names_costs[key] = value

    max_damages = max(names_costs.values())
    damage_cost = {}
    for key, value in names_costs.items():
        if value == max_damages:
            damage_cost[key] = value
    return damage_cost


g_damage_cost = greatest_damages_and_cost(names, updated_damage)
print(g_damage_cost)
# write your catgeorize by damage function here:
def hurricanes_damage_scale(damages):
    damages_rate = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for values in damages:
        if values == "Damages not recorded":
            values = 0
        for key, value in damages_rate.items():
            if key == 0 and values <= 0:
                key = values
            elif key == 1 and 0 < values <= 100000000:
                key = value.append(values)
            elif key == 2 and 100000000 < values <= 1000000000:
                key = value.append(values)
            elif key == 3 and 1000000000 < values <= 10000000000:
                key = value.append(values)
            elif key == 4 and 10000000000 < values <= 50000000000:
                key = value.append(values)
            elif key == 5 and values > 50000000000:
                key = value.append(values)
    return damages_rate


damage_scale = hurricanes_damage_scale(updated_damage)
print(damage_scale)
