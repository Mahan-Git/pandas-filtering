import os
import numpy as np

class Filter(object):
    def __init__(self, plant_database, images_folderpath):
        self._keys_list = None
        self._values_list = None
        self.database = plant_database
        self.df = plant_database.db
        self.names = []
        self.paths = []
        self.images_folderpath = images_folderpath
        # MAKE THIS READ NUM OF ROWS
        self._num_plant_Database = 5613
        # self._keys_list = list(self.dict)
        # self._values_list = list(self.dict.values())
        self._elevation_ranges = []
        self._elevation_ranges_str = []
        self._seed_ranges = []
        self._seed_ranges_str = []
        self._hight_average_tol = 0.50
        self._width_average_tol = 0.50
        self.clean_df()
        self.names = []
        self.paths = []

    def clean_df(self):
        range_str = []
        seed_range_str = []
        counter = 0
        lowest_point_on_earth = -413
        highest_point_on_earth = 8848
        # turn the elevation ranges to number
        for i in range(1, len(self.df.columns)):
            if self.df.columns[i] == 'Elevation range(m)':
                counter = 0
                self._elevation_ranges_cul_num = i
                for j in range(1, self._num_plant_Database):
                    #storing dataframe to filter by string value later
                    self._elevation_ranges_str.append(self.df.iloc[j, self._elevation_ranges_cul_num])
                    if (isinstance(self._elevation_ranges_str[j-1], str) and self._elevation_ranges_str[j-1] != float('nan') and self._elevation_ranges_str[j-1] != 'nan'):
                        if (' - ' in self._elevation_ranges_str[j-1]):
                            range_str.append(str(self._elevation_ranges_str[j-1]).partition(' - '))
                            counter += 1
                            if range_str[counter - 1] is not None:
                                if range_str[counter - 1][0] != '' and range_str[counter - 1][2] != '':
                                    if float(range_str[counter - 1][0]) > float(range_str[counter - 1][2]):
                                        self._elevation_ranges.append(
                                            [float(range_str[counter - 1][2]), float(range_str[counter - 1][0]), j])
                                    else:
                                        self._elevation_ranges.append(
                                            [float(range_str[counter - 1][0]), float(range_str[counter - 1][2]), j])
                                else:
                                    self._elevation_ranges.append([float('nan'), float('nan'), j])
                                    print("else 1 Failed to convert for ' - ':", j,
                                          "and column:",
                                          self._elevation_ranges_cul_num, 'values is:',
                                          self._elevation_ranges_str[j - 1])
                            else:
                                self._elevation_ranges.append([float('nan'), float('nan'), j])
                                print("else 2 Failed to convert for ' - ':", j,
                                      "and column:",
                                      self._elevation_ranges_cul_num, 'values is:',
                                      self._elevation_ranges_str[j - 1])
                        elif ('- ' in self._elevation_ranges_str[j-1]):
                            range_str.append(str(self._elevation_ranges_str[j-1]).partition('- '))
                            counter += 1
                            if range_str[counter - 1] is not None:
                                if range_str[counter - 1][0] != '' and range_str[counter - 1][2] != '':
                                    if float(range_str[counter - 1][0]) > float(range_str[counter - 1][2]):
                                        self._elevation_ranges.append(
                                            [float(range_str[counter - 1][2]), float(range_str[counter - 1][0]), j])
                                    else:
                                        self._elevation_ranges.append(
                                            [float(range_str[counter - 1][0]), float(range_str[counter - 1][2]), j])
                                else:
                                    self._elevation_ranges.append([float('nan'), float('nan'), j])
                                    print("else 1 Failed to convert for '- ':", j,
                                          "and column:",
                                          self._elevation_ranges_cul_num, 'values is:',
                                          self._elevation_ranges_str[j - 1])
                            else:
                                self._elevation_ranges.append([float('nan'), float('nan'), j])
                                print("else 2 Failed to convert for '- ':", j,
                                      "and column:",
                                      self._elevation_ranges_cul_num, 'values is:',
                                      self._elevation_ranges_str[j - 1])
                        elif ('-' in self._elevation_ranges_str[j-1]):
                            range_str.append(str(self._elevation_ranges_str[j-1]).partition('-'))
                            counter += 1
                            if range_str[counter - 1] is not None:
                                if range_str[counter - 1][0] != '' and range_str[counter - 1][2] != '':
                                    if float(range_str[counter - 1][0]) > float(range_str[counter - 1][2]):
                                        self._elevation_ranges.append(
                                            [float(range_str[counter - 1][2]), float(range_str[counter - 1][0]), j])
                                    else:
                                        self._elevation_ranges.append(
                                            [float(range_str[counter - 1][0]), float(range_str[counter - 1][2]), j])
                                else:
                                    self._elevation_ranges.append([float('nan'), float('nan'), j])
                                    print("else 1 Failed to convert for '-':", j,
                                          "and column:",
                                          self._elevation_ranges_cul_num, 'values is:',
                                          self._elevation_ranges_str[j - 1])
                            else:
                                self._elevation_ranges.append([float('nan'), float('nan'), j])
                                print("else 2 Failed to convert for '-':", j,
                                      "and column:",
                                      self._elevation_ranges_cul_num, 'values is:',
                                      self._elevation_ranges_str[j - 1])
                        elif ('≤' in self._elevation_ranges_str[j-1]):
                            range_str.append(str(self._elevation_ranges_str[j-1]).partition('≤ '))
                            counter += 1
                            if range_str[counter - 1][2] != '':
                                self._elevation_ranges.append([lowest_point_on_earth, float(range_str[counter - 1][2]), j])
                            else:
                                self._elevation_ranges.append([float('nan'), float('nan'), j])
                                print("Failed to convert for ≤:", j,
                                      "and column:",
                                      self._elevation_ranges_cul_num, 'values is:',
                                      self._elevation_ranges_str[j - 1])
                        elif ('<' in self._elevation_ranges_str[j-1]):
                            range_str.append(str(self._elevation_ranges_str[j-1]).partition('< '))
                            counter += 1
                            if range_str[counter - 1][2] != '':
                                self._elevation_ranges.append([lowest_point_on_earth, float(range_str[counter - 1][2]), j])
                            else:
                                self._elevation_ranges.append([float('nan'), float('nan'), j])
                                print("Failed to convert for <:", j,
                                      "and column:",
                                      self._elevation_ranges_cul_num, 'values is:',
                                      self._elevation_ranges_str[j - 1])
                        elif ('>' in self._elevation_ranges_str[j-1]):
                            range_str.append(str(self._elevation_ranges_str[j-1]).partition('> '))
                            counter += 1
                            if range_str[counter - 1][2] != '':
                                self._elevation_ranges.append([float(range_str[counter - 1][2]), highest_point_on_earth, j])
                            else:
                                self._elevation_ranges.append([float('nan'), float('nan'), j])
                                print("Failed to convert for >:", j,
                                      "and column:",
                                      self._elevation_ranges_cul_num, 'values is:',
                                      self._elevation_ranges_str[j - 1])
                        else:
                            self._elevation_ranges.append([float('nan'), float('nan'), j])
                    else:
                        self._elevation_ranges.append([float('nan'), float('nan'), j])
            elif self.df.columns[i] == 'Seed viability(years)':
                counter = 0
                self._seed_ranges_cul_num = i
                for j in range(1, self._num_plant_Database):
                    #storing dataframe to filter by string value later
                    self._seed_ranges_str.append(self.df.iloc[j, self._seed_ranges_cul_num])
                    if (isinstance(self._seed_ranges_str[j-1], str) and self._seed_ranges_str[j-1] != float('nan') and self._seed_ranges_str[j-1] != 'nan'):
                        if ('up to ' in self._seed_ranges_str[j-1]):
                            seed_range_str.append(str(self._seed_ranges_str[j-1]).partition('up to '))
                            counter += 1
                            if seed_range_str[counter - 1][2] != '':
                                self._seed_ranges.append([0, float(seed_range_str[counter - 1][2]), j])
                            else:
                                self._seed_ranges.append([float('nan'), float('nan'), j])
                                print("Failed to convert for ≤:", j,
                                      "and column:",
                                      self._seed_ranges_cul_num, 'values is:',
                                      self._seed_ranges_str[j - 1])
                        elif (' to ' in self._seed_ranges_str[j-1]):
                            #if not (',' in self._seed_ranges_str[j-1]):
                            seed_range_str.append(str(self._seed_ranges_str[j-1]).partition(' to '))
                            counter += 1
                            if seed_range_str[counter - 1] is not None:
                                if seed_range_str[counter - 1][2] != '':
                                    self._seed_ranges.append(
                                        [0, float(seed_range_str[counter - 1][2]),  j])
                        elif ('<' in self._seed_ranges_str[j-1]):
                            seed_range_str.append(str(self._seed_ranges_str[j-1]).partition('<'))
                            counter += 1
                            if seed_range_str[counter - 1][2] != '':
                                self._seed_ranges.append([0, float(seed_range_str[counter - 1][2]), j])
                            else:
                                self._seed_ranges.append([float('nan'), float('nan'), j])
                                print("Failed to convert for <:", j,
                                      "and column:",
                                      self._seed_ranges_cul_num, 'values is:',
                                      self._seed_ranges_str[j - 1])
                        else:
                            self._seed_ranges.append([float('nan'), float('nan'), j])
                    elif isinstance(self._seed_ranges_str[j-1], int):
                        self._seed_ranges.append([0, float(self._seed_ranges_str[j-1]), j])
                    else:
                        self._seed_ranges.append([float('nan'), float('nan'), j])
    def filter_df(self, dict):
        self._keys_list = list(dict)
        self._values_list = list(dict.values())
        # turn dictionary to list for iteration, and getting keys or values by index
        # answers = self.proj.answers
        elevation_ranges_filter = []
        seed_ranges_filter = []
        plant_type_filter = []
        suitable_site_filter = []
        native_habitat_filter = []
        duration_filter = []
        lifespan_filter = []
        growth_speed_filter = []
        growth_period_filter = []
        foliage_color_filter = []
        autumn_color_filter =[]
        shape_filter = []
        root_system_filter = []
        flowering_period_filter = []
        flower_color_filter = []
        fruiting_period_filter = []
        fruit_type_filter = []
        light_requirements_filter = []
        soil_moisture_filter = []
        Soil_ph_filter = []
        type_soil_filter = []
        fauna_association_filter = []
        other_conditions_filter = []
        propagation_methodology_filter = []
        df_clone = self.df
        #clean dataframe from non Plant data
        df_clone = df_clone.drop(index=df_clone.index[0])
        df_clone = df_clone.drop(index=df_clone.index[self._num_plant_Database:len(df_clone.index)])
        for i in range(len(self._keys_list)):
            if not ((self._values_list[i]) == None and type(self._values_list[i]) is str and self._values_list[i] == ""):
                # if len(self._values_list[i]) == 1:
                #     self._values_list[i] = self._values_list[i][0]
                if self._keys_list[i] == 'Min height(m)' or self._keys_list[i] == 'Min width(m)' or self._keys_list[i] == 'Carbon storage(kg)':
                    try:
                        df_clone = df_clone[df_clone[self._keys_list[i]] >= float(self._values_list[i])]
                    except:
                        print("failed to filter ", self._keys_list[i], ":", self._values_list[i])
                elif self._keys_list[i] == 'Max height(m)' or self._keys_list[i] == 'Max width(m)':
                    try:
                        df_clone = df_clone[df_clone[self._keys_list[i]] <= float(self._values_list[i])]
                    except:
                        print("failed to filter ", self._keys_list[i], ":", self._values_list[i])
                elif self._keys_list[i] == 'Average height(m)':
                    try:
                        df_clone = df_clone[df_clone[self._keys_list[i]] >= (float(self._values_list[i]) - self._hight_average_tol)]
                        df_clone = df_clone[df_clone[self._keys_list[i]] <= (float(self._values_list[i]) + self._hight_average_tol)]
                    except:
                        print("failed to filter ", self._keys_list[i], ":", self._values_list[i])
                elif self._keys_list[i] == 'Average width(m)':
                    try:
                        df_clone = df_clone[df_clone[self._keys_list[i]] >= (float(self._values_list[i]) - self._width_average_tol)]
                        df_clone = df_clone[df_clone[self._keys_list[i]] <= (float(self._values_list[i]) + self._width_average_tol)]
                    except:
                        print("failed to filter ", self._keys_list[i], ":", self._values_list[i])
                elif self._keys_list[i] == 'Recommended number of individuals per square meter':
                    try:
                        df_clone = df_clone[df_clone[self._keys_list[i]] <= float(self._values_list[i])]
                    except:
                        print("failed to filter ", self._keys_list[i], ":", self._values_list[i])
                elif self._keys_list[i] == 'Elevation range(m)':
                    #try:
                    for j in range(len(self._elevation_ranges)):
                        if (self._elevation_ranges[j][0] != float('nan') and self._elevation_ranges[j][0] != np.nan and self._elevation_ranges[j][0] !='nan' and self._elevation_ranges[j][1] !='nan' and self._elevation_ranges[j][1] != float('nan')  and self._elevation_ranges[j][1] != np.nan and self._values_list[i] != 'nan' and self._values_list[i] != float('nan')  and self._values_list[i] != np.nan):
                            if float(self._elevation_ranges[j][0]) < float(self._values_list[i]) < float(self._elevation_ranges[j][1]):
                                try:
                                    elevation_ranges_filter.append(self._elevation_ranges_str[j])
                                except:
                                    print("it is in range but failed to filter", "Elevation range", " at row", j, "for the range", self._elevation_ranges_str[j])
                        else:
                            print('Failed to Filter NaN value', " at row", j,)
                elif self._keys_list[i] == 'Seed viability(years)':
                    for j in range(len(self._seed_ranges)):
                        if (self._seed_ranges[j][0] != float('nan') and self._seed_ranges[j][0] != np.nan and self._seed_ranges[j][0] != 'nan' and self._seed_ranges[j][1] != 'nan' and self._seed_ranges[j][1] != float('nan') and self._seed_ranges[j][1] != np.nan and self._values_list[i] != 'nan' and self._values_list[i] != float('nan') and self._values_list[i] != np.nan):
                            if float(self._seed_ranges[j][0]) < float(self._values_list[i]) < float(self._seed_ranges[j][1]):
                                try:
                                    seed_ranges_filter.append(self._seed_ranges_str[j])
                                except:
                                    print("it is in range but failed to filter", "Seed viability range", " at row", j,
                                          "for the range", self._seed_ranges_str[j])
                        else:
                            print('Failed to Filter NaN value', " at row", j, )
                ###############################################################################################
                #multiple values in the culumns like: short- short,moderate - moderate,long - ...
                ###############################################################################################
                elif self._keys_list[i] == 'Plant type':
                    try:
                        idx = self.df.columns.get_loc('Plant type')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    plant_type_filter.append(self.df.iloc[j, idx])
                        if not plant_type_filter:
                            plant_type_filter = None
                    except:
                        print("could not Filter Plant type")
                elif self._keys_list[i] == 'Suitable site':
                    try:
                        idx = self.df.columns.get_loc('Suitable site')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    suitable_site_filter.append(self.df.iloc[j, idx])
                        if not suitable_site_filter:
                            suitable_site_filter = None
                    except:
                        print("could not Filter Suitable site")
                elif self._keys_list[i] == 'Native habitat':
                    try:
                        idx = self.df.columns.get_loc('Native habitat')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    native_habitat_filter.append(self.df.iloc[j, idx])
                        if not native_habitat_filter:
                            native_habitat_filter = None
                    except:
                        print("could not Filter Native habitat")
                elif self._keys_list[i] == 'Duration':
                    try:
                        idx = self.df.columns.get_loc('Duration')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    duration_filter.append(self.df.iloc[j, idx])
                        if not duration_filter:
                            duration_filter = None
                    except:
                        print("could not Filter Duration")
                elif self._keys_list[i] == 'Lifespan':
                    try:
                        idx = self.df.columns.get_loc('Lifespan')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    lifespan_filter.append(self.df.iloc[j, idx])
                        if not lifespan_filter:
                            lifespan_filter = None
                    except:
                        print("could not Filter Lifespan")
                elif self._keys_list[i] == 'Growth speed':
                    try:
                        idx = self.df.columns.get_loc('Growth speed')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    growth_speed_filter.append(self.df.iloc[j, idx])
                        if not growth_speed_filter:
                            growth_speed_filter = None
                    except:
                        print("could not Filter Growth speed")
                elif self._keys_list[i] == 'Active growth period':
                    try:
                        idx = self.df.columns.get_loc('Active growth period')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    growth_period_filter.append(self.df.iloc[j, idx])
                        if not growth_period_filter:
                            growth_period_filter = None
                    except:
                        print("could not Filter Active growth period")
                elif self._keys_list[i] == 'Foliage color':
                    try:
                        idx = self.df.columns.get_loc('Foliage color')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    foliage_color_filter.append(self.df.iloc[j, idx])
                        if not foliage_color_filter:
                            foliage_color_filter = None
                    except:
                        print("could not Filter Foliage color")
                elif self._keys_list[i] == 'Autumn color change':
                    try:
                        idx = self.df.columns.get_loc('Autumn color change')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    autumn_color_filter.append(self.df.iloc[j, idx])
                        if not autumn_color_filter:
                            autumn_color_filter = None
                    except:
                        print("could not Filter Autumn color change")
                elif self._keys_list[i] == 'Shape':
                    try:
                        idx = self.df.columns.get_loc('Shape')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    shape_filter.append(self.df.iloc[j, idx])
                        if not shape_filter:
                            shape_filter = None
                    except:
                        print("could not Filter Shape")
                elif self._keys_list[i] == 'Root system':
                    try:
                        idx = self.df.columns.get_loc('Root system')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    root_system_filter.append(self.df.iloc[j, idx])
                        if not root_system_filter:
                            root_system_filter = None
                    except:
                        print("could not Filter Root system")
                elif self._keys_list[i] == 'Flowering period':
                    try:
                        idx = self.df.columns.get_loc('Flowering period')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    flowering_period_filter.append(self.df.iloc[j, idx])
                        if not flowering_period_filter:
                            flowering_period_filter = None
                    except:
                        print("could not Filter Flowering period")
                elif self._keys_list[i] == 'Flower color':
                    try:
                        idx = self.df.columns.get_loc('Flower color')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    flower_color_filter.append(self.df.iloc[j, idx])
                        if not flower_color_filter:
                            flower_color_filter = None
                    except:
                        print("could not Filter Flower color")
                elif self._keys_list[i] == 'Fruiting period':
                    try:
                        idx = self.df.columns.get_loc('Fruiting period')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    fruiting_period_filter.append(self.df.iloc[j, idx])
                        if not fruiting_period_filter:
                            fruiting_period_filter = None
                    except:
                        print("could not Filter Fruiting period")
                elif self._keys_list[i] == 'Fruit type':
                    try:
                        idx = self.df.columns.get_loc('Fruit type')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    fruit_type_filter.append(self.df.iloc[j, idx])
                        if not fruit_type_filter:
                            fruit_type_filter = None
                    except:
                        print("could not Filter Fruit type")
                elif self._keys_list[i] == 'Light requirements':
                    try:
                        idx = self.df.columns.get_loc('Light requirements')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    light_requirements_filter.append(self.df.iloc[j, idx])
                        if not light_requirements_filter:
                            light_requirements_filter = None
                    except:
                        print("could not Filter Light requirements")
                elif self._keys_list[i] == 'Soil moisture level':
                    try:
                        idx = self.df.columns.get_loc('Soil moisture level')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    soil_moisture_filter.append(self.df.iloc[j, idx])
                        if not soil_moisture_filter:
                            soil_moisture_filter = None
                    except:
                        print("could not Filter Soil moisture level")
                elif self._keys_list[i] == 'Soil pH':
                    try:
                        idx = self.df.columns.get_loc('Soil pH')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    Soil_ph_filter.append(self.df.iloc[j, idx])
                        if not Soil_ph_filter:
                            Soil_ph_filter = None
                    except:
                        print("could not Filter Soil pH")
                elif self._keys_list[i] == 'Type soil':
                    try:
                        idx = self.df.columns.get_loc('Type soil')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    type_soil_filter.append(self.df.iloc[j, idx])
                        if not type_soil_filter:
                            type_soil_filter = None
                    except:
                        print("could not Filter Type soil")
                elif self._keys_list[i] == 'Fauna association':
                    try:
                        idx = self.df.columns.get_loc('Fauna association')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    fauna_association_filter.append(self.df.iloc[j, idx])
                        if not fauna_association_filter:
                            fauna_association_filter = None
                    except:
                        print("could not Filter Fauna association")
                elif self._keys_list[i] == 'Other conditions':
                    try:
                        idx = self.df.columns.get_loc('Other conditions')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    other_conditions_filter.append(self.df.iloc[j, idx])
                        if not other_conditions_filter:
                            other_conditions_filter = None
                    except:
                        print("could not Filter Other conditions")
                elif self._keys_list[i] == 'Propagation methodology':
                    try:
                        idx = self.df.columns.get_loc('Propagation methodology')
                        for value in self._values_list[i]:
                            for j in range(self._num_plant_Database):
                                if str(value) in str(self.df.iloc[j, idx]):
                                    propagation_methodology_filter.append(self.df.iloc[j, idx])
                        if not propagation_methodology_filter:
                            propagation_methodology_filter = None
                    except:
                        print("could not Filter Propagation methodology")
                ###############################################################################################
                #Single values in the column like: deciduous - evergreen - ...
                ###############################################################################################
                elif self._keys_list[i] == 'Foliage retention' or self._keys_list[i] == 'Leaf type' or self._keys_list[i] == 'Aggressive roots' or self._keys_list[i] == 'Scent' or self._keys_list[i] == 'Flower type' or self._keys_list[i] == 'Fruit type' or self._keys_list[i] == 'Culinary value' or self._keys_list[i] == 'Medicinal value' or self._keys_list[i] == 'Soil depth' or self._keys_list[i] == 'Waterlogging tolerance' or self._keys_list[i] == 'Wind tolerance' or self._keys_list[i] == 'Toxicity' or self._keys_list[i] == 'Allergy inducing' or self._keys_list[i] == 'Maintenance level' or self._keys_list[i] == 'Watering needs' or self._keys_list[i] == 'Watering needs' or self._keys_list[i] == 'Fruit/Leaf/FlowerLitter' or self._keys_list[i] == 'Resistant to vandalism' or self._keys_list[i] == 'Propagation difficulty':
                    try:
                        if isinstance(self._values_list[i], list):
                            df_clone = df_clone[df_clone[self._keys_list[i]].isin(self._values_list[i])]
                        else:
                            df_clone = df_clone[df_clone[self._keys_list[i]] == (self._values_list[i])]
                    except:
                        print("could not Filter by matching the value")
                elif self._keys_list[i] == 'LAI':
                    try:
                        df_clone = df_clone[df_clone[self._keys_list[i]] == float(self._values_list[i])]
                    except:
                        print("could not Filter LAI")

        #elevation range Filter should be out of the loop and applied as a list
        # next line for including "nan" values
        #elevation_ranges_filter.append(np.nan)
        if elevation_ranges_filter:
            df_clone = df_clone[df_clone['Elevation range(m)'].isin(elevation_ranges_filter)]
        if seed_ranges_filter:
            df_clone = df_clone[df_clone['Seed viability(years)'].isin(seed_ranges_filter)]
        ###############################################################################################
        #region Filter multiple values columns
        ###############################################################################################
        # TO DO make all feature of the same filter category into a string list, then iterate
        if plant_type_filter:
            df_clone = df_clone[df_clone['Plant type'].isin(plant_type_filter)]
        if suitable_site_filter:
            df_clone = df_clone[df_clone['Suitable site'].isin(suitable_site_filter)]
        if native_habitat_filter:
            df_clone = df_clone[df_clone['Native habitat'].isin(native_habitat_filter)]
        if duration_filter:
            df_clone = df_clone[df_clone['Duration'].isin(duration_filter)]
        if lifespan_filter:
            df_clone = df_clone[df_clone['Lifespan'].isin(lifespan_filter)]
        if growth_speed_filter:
            df_clone = df_clone[df_clone['Growth speed'].isin(growth_speed_filter)]
        if growth_period_filter:
            df_clone = df_clone[df_clone['Active growth period'].isin(growth_period_filter)]
        if foliage_color_filter:
            df_clone = df_clone[df_clone['Foliage color'].isin(foliage_color_filter)]
        if autumn_color_filter:
            df_clone = df_clone[df_clone['Autumn color change'].isin(autumn_color_filter)]
        if shape_filter:
            df_clone = df_clone[df_clone['Shape'].isin(shape_filter)]
        if root_system_filter:
            df_clone = df_clone[df_clone['Root system'].isin(root_system_filter)]
        if flowering_period_filter:
            df_clone = df_clone[df_clone['Flowering period'].isin(flowering_period_filter)]
        if flower_color_filter:
            df_clone = df_clone[df_clone['Flower color'].isin(flower_color_filter)]
        if fruiting_period_filter:
            df_clone = df_clone[df_clone['Fruiting period'].isin(fruiting_period_filter)]
        if fruit_type_filter:
            df_clone = df_clone[df_clone['Fruit type'].isin(fruit_type_filter)]
        if light_requirements_filter:
            df_clone = df_clone[df_clone['Light requirements'].isin(light_requirements_filter)]
        if soil_moisture_filter:
            df_clone = df_clone[df_clone['Soil moisture level'].isin(soil_moisture_filter)]
        if Soil_ph_filter:
            df_clone = df_clone[df_clone['Soil pH'].isin(Soil_ph_filter)]
        if type_soil_filter:
            df_clone = df_clone[df_clone['Type soil'].isin(type_soil_filter)]
        if fauna_association_filter:
            df_clone = df_clone[df_clone['Fauna association'].isin(fauna_association_filter)]
        if other_conditions_filter:
            df_clone = df_clone[df_clone['Other conditions'].isin(other_conditions_filter)]
        if propagation_methodology_filter:
            df_clone = df_clone[df_clone['Propagation methodology'].isin(propagation_methodology_filter)]
        if plant_type_filter == None or suitable_site_filter == None or native_habitat_filter == None or duration_filter == None or lifespan_filter == None or growth_speed_filter == None or growth_period_filter == None or foliage_color_filter == None or autumn_color_filter == None or shape_filter == None or root_system_filter == None or flowering_period_filter == None or flower_color_filter == None or fruiting_period_filter == None or fruit_type_filter == None or light_requirements_filter == None or soil_moisture_filter == None or Soil_ph_filter == None or type_soil_filter == None or fauna_association_filter == None or other_conditions_filter == None or propagation_methodology_filter == None:
            df_clone = df_clone[df_clone[self._keys_list[i]] == ('none')]
        #endregion

        # filter plants names
        # Clear lists
        del self.names[:]
        del self.paths[:]

        for i in range(0, len(df_clone.iloc[:, 1])):
            self.names.append(df_clone.iloc[i, 0])
        # get filtered plants paths
        images = os.listdir(self.images_folderpath)
        for i in self.names:
            i = str(i) + ".png"
            if i in images:
                self.paths.append(os.path.join(self.images_folderpath, i))
            else:
                self.paths.append(os.path.join(self.images_folderpath, 'noimage.png'))

# Method to call
# obj = Filter(current_project, database, images_folderpath)
#obj.filter_df()

# attributes of the object to access are names, and paths
#obj.names
#obj.paths