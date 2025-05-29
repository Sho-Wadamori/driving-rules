# Driving Rule Database

### Overview
This program provides a collection of driving rules and regulations for all* countries. It includes information such as the driving side, minimum driving license age, and alcohol limit. 

**This program can:** 
Search for specific countries
Get general statistics
List the database with tools such as: 
- Ordering
- Filtering
- styling of the output

These Tools allow for the best way to view the information.

>**If you see this message:**
>```
>'tabulate' installed successfully. Please restart the program.
>```
> **Please restart the program**
---

### Original Data Source
**World Population Review:** Began by sourcing information from [worldpopulationreview.com](https://worldpopulationreview.com), but it lacked data for certain countries, included non-country territories, and contained some inaccuracies. Only country codes and names were kept from this source. For these reasons, the data source was changed to Wikipedia due to its constant updates, as well as explanations and arguments supporting their decisions. 

*While the accuracy of Wikipedia is often questioned due to it being editable by anyone, controversial pages such as ones used in this database are protected, meaning all changes and decisions need to be supported by proper evidence and support.*

---

### Deisions Made
- **Country List:** The list was only taken from the "UN member states and General Assembly observer states" section due to various reasons. When searching for "how many countries are there", or something similar, the number 195 usually comes up (the number of UN members and observers). This is also the most commonly used and agreed list for the specific criteria. <ins>This does not mean other regions are not countries</ins>, but just did not meet the criteria I set for this database.
  - For more information, please visit the [Wikipedia talk page](https://en.wikipedia.org/wiki/Talk:List_of_sovereign_states), which has all the details on the their reasonings and arguments.

- **Driving Side:** In cases where driving rules are different inside a country (e.g., overseas territories), the capital city's rules are used as the default.  
  **Example:**  
  - **United Kingdom**: Primarily left side, but some overseas territories, such as the British Indian Ocean Territory, drives on the right.

- **Minimum Licence Age:** The list shows the minimum age to obtain any type of car licence (including learner's/provisional licences) in the **capital city** of each country. Additionally, the age is **rounded down**.
  **Example:** 
  - **Canada**: The minimum age to obtain a driver's licence is 16 in Ottawa (the capital), but is 14 in Alberta.
  - **Australia**: The minimum age to obtain a learner's licence is 15 years and 9 months in Canberra/ACT (the capital). The age for Australia is set to 15 years old.

---

### Data Sources
- **ALPHA-2 CODE:** This data is from the [IBAN Country Codes](https://www.iban.com/country-codes) website.  
- **Country List:** This list of sovereign is taken from  [Wikipedia's List of Sovereign states](https://en.wikipedia.org/wiki/List_of_sovereign_states#List_of_states).  
- **Driving Side:** This data is from the [Wikipedia on Left- and Right-Hand Traffic](https://en.wikipedia.org/wiki/Left-_and_right-hand_traffic) page.
- **Minimum Licence Age:** This data is from the [Wikipedia List of Minimum Driving Ages](https://en.wikipedia.org/wiki/List_of_minimum_driving_ages) page.
- **Alcohol Limit:** This data is from the [Wikipedia Drunk driving law by country](https://en.wikipedia.org/wiki/Drunk_driving_law_by_country) page.
- **Max Speed:** This data is from the [Wikipedia Speed limits by country](https://en.wikipedia.org/wiki/Speed_limits_by_country) table.

---

### Special Considerations
##### Country List:
- Removed *The Republic of* and other prefixes for the sake of simplicity.
- **Ivory Coast**: Officially known as **Côte d'Ivoire**, but commonly referred to as Ivory Coast with English speakers.
- **Czech Republic**: Sometimes called **Czechia**.  
- **Democratic Republic of the Congo** and **Republic of the Congo**: Kept the official names to avoid confusion between the two.  
- **Turkey**: Recently changed its name to **Türkiye**, but for ease of recognition, "Turkey" is used here.  
- **Cape Verde**: Officially known as **Cabo Verde**, but is more commonly known as **Cape Verde** with English speakers.  
- **Micronesia**: Officially **Federated States of Micronesia** but kept as simply **Micronesia** for convenience.

##### Driving Side:
- **China:** Is left side in Hong Kong and Maccau but not in mainland and the Capital (Beijing)
- **United Kingdom:** Is right side in *British Indian Ocean Territory* and *Gibraltar* but is left side everywhere else (including the capital London)
- **United States:** Is left in U.S. Virgin Islands but right everywhere else

##### Minimum Licence Age:
- **Australia:** Depends on state, 15 in Canberra (Capital). Rounded down 15 years 9 months.
- **Canada:** Depends on state, 16 in Ottawa (Capital).
- **Israel:** Rounded down 16 years 6 months.
- **Northern Mariana Islands:** Rounded down 15 years 6 months.
- **United States:** Depends on state, 16 in Washington DC (Capital).

##### Max Speed:
- **China:** - 120km/h
  - Hong Kong	- 110km/h
  - Macau	- 80km/h
  - Taiwan - 110km/h
- **Denmark:** - 130km/h
  - Faroe Islands	- 80km/h
  - Greenland	- 80km/h
- **Finland:** - 120km/h
  - Åland	- 90km/h
---

### Removed Countries
Territories that were excluded due to conflicts between data from **World Population Review** and **Wikipedia**. 

| Name | Reason |
| - | - |
| Guadeloupe | French Territory. |
| Guam | US Territory. |
| Greenland | Danish Territory. |
| Hong Kong | Chinese Territory. |
| New Caledonia | French Territory. |
| Puerto Rico | US Territory. |
| Taiwan | Not included in the UN member states list on Wikipedia. |

Territories that were excluded due to conflicts between data from **Wikipedia List of minimum driving ages** and **Wikipedia List of sovereign states**. 
| Name | Reason | 
| - | - |               
| Cayman Islands | British Territory | 
| Curaçao | Duch Territory | 
| Falkland Islands | British Territory | 
| French Guiana | French Territory | 
| Gibraltar | British Territory | 
| Guadeloupe | French Territoy | 
| Guam | US Territory | 
| Guernsey | British Territory | 
| Hong Kong | Chinese Territory | 
| Isle of Man | British Dependency | 
| Jersey | British Dependency | 
| Kosovo | Not in list of UN member states and General Assembly observer states | 
| Macau | Special administrative region of China | 
| Martinique | French Territoy | 
| Mayotte | French Territoy | 
| Northern Cyprus | Cyprus Territory | 
| Northern Mariana Islands | US Territory | 
| Puerto Rico | US Territory | 
| Saint Barthélemy | French Territoy | 
| Saint Martin | French Territoy | 
| Taiwan | Not in list of UN member states and General Assembly observer states | 
| US Virgin Islands | US Territory | 

---

### Added Data
Many countries were added that were missing from **World Population Review**'s data. These countries are: 

|                      |                       |                                  |                                  |
| -------------------- | --------------------- | -------------------------------- | -------------------------------- |
| Afghanistan          | Albania               | Antigua and Barbuda              | Armenia                          |
| Benin                | Bhutan                | Brunei                           | Burkina Faso                     |
| Burundi              | Cape Verde            | Central African Republic         | Chad                             |
| Comoros              | Cuba                  | Democratic Republic of the Congo | Djibouti                         |
| Equatorial Guinea    | Eritrea               | Eswatini                         | Ethiopia                         |
| Gambia               | Grenada               | Guinea                           | Guinea-Bissau                    |
| Guyana               | Iran                  | Iraq                             | Ivory Coast                      |
| Kazakhstan           | Kiribati              | Kyrgyzstan                       | Liberia                          |
| Libya                | Liechtenstein         | Madagascar                       | Maldives                         |
| Marshall Islands     | Mauritania            | Micronesia                       | Monaco                           |
| Mongolia             | Myanmar               | Nauru                            | Nepal                            |
| Niger                | North Korea           | Palau                            | Palestine                        |
| Russia               | Rwanda                | Saint Kitts and Nevis            | Saint Vincent and the Grenadines |
| San Marino           | São Tomé and Príncipe | Sierra Leone                     | Solomon Islands                  |
| Somalia              | South Sudan           | Sudan                            | Suriname                         |
| Timor-Leste          | Tonga                 | Turkmenistan                     | Tuvalu                           |
| United Arab Emirates | United States         | Uzbekistan                       | Vatican City                     |

<br>

Many countries were missing from **Wikipedia List of minimum driving ages**. These countries are:

|                   |                                  |                          |                                  |
| ----------------- | -------------------------------- | ------------------------ | -------------------------------- |
| Angola            | Antigua and Barbuda              | Barbados                 | Belize                           |
| Benin             | Bhutan                           | Botswana                 | Burkina Faso                     |
| Burundi           | Cape Verde                       | Central African Republic | Chad                             |
| Comoros           | Democratic Republic of the Congo | Djibouti                 | Dominica                         |
| Equatorial Guinea | Eritrea                          | Gabon                    | Gambia                           |
| Grenada           | Guinea                           | Guinea-Bissau            | Haiti                            |
| Ivory Coast       | Kazakhstan                       | Kiribati                 | Kyrgyzstan                       |
| Liberia           | Madagascar                       | Malawi                   | Micronesia                       |
| Mongolia          | Nauru                            | North Korea              | Palau                            |
| Palestine         | Republic of the Congo            | Saint Lucia              | Saint Vincent and the Grenadines |
| Samoa             | São Tomé and Príncipe            | Singapore                | Slovakia                         |
| Solomon Islands   | Somalia                          | South Sudan              | Sudan                            |
| Tajikistan        | Timor-Leste                      | Tonga                    | Turkmenistan                     |
| Tuvalu            | Uzbekistan                       | Vanuatu                  | Vatican City                     |

<br>

More than half the countries in the list were missing from **Wikipedia Speed limits by country**. These countries were **MANUALLY SEARCHED UP AND INPUTTED**, meaning the data is **VERY VERY VERY INNACURATE**. The main sources are Google, WHO, internationaldriversassociation.com, and worlddata.info. These countries are:

|                       |                       |                                  |                                  |
| --------------------- | --------------------- | -------------------------------- | -------------------------------- |
| Afghanistan           | Algeria               | Andorra                          | Angola                           |
| Antigua and Barbuda   | Armenia               | Bahamas                          | Barbados                         |
| Belize                | Benin                 | Bhutan                           | Bolivia                          |
| Botswana              | Burkina Faso          | Burundi                          | Cambodia                         |
| Cameroon              | Cape Verde            | Central African Republic         | Chad                             |
| Colombia              | Comoros               | Cuba                             | Democratic Republic of the Congo |
| Djibouti              | Dominica              | Dominican Republic               | Ecuador                          |
| El Salvador           | Equatorial Guinea     | Eritrea                          | Eswatini                         |
| Ethiopia              | Fiji                  | Gabon                            | Gambia                           |
| Ghana                 | Grenada               | Guatemala                        | Guinea                           |
| Guinea-Bissau         | Guyana                | Haiti                            | Honduras                         |
| Iraq                  | Ivory Coast           | Jamaica                          | Kenya                            |
| Kiribati              | Kuwait                | Kyrgyzstan                       | Laos                             |
| Lesotho               | Liberia               | Libya                            | Madagascar                       |
| Malawi                | Maldives              | Mali                             | Marshall Islands                 |
| Mauritania            | Mauritius             | Micronesia                       | Monaco                           |
| Mongolia              | Montenegro            | Mozambique                       | Myanmar                          |
| Namibia               | Nauru                 | Nepal                            | Nicaragua                        |
| Niger                 | Nigeria               | North Korea                      | Oman                             |
| Palau                 | Palestine             | Panama                           | Papua New Guinea                 |
| Paraguay              | Qatar                 | Republic of the Congo            | Rwanda                           |
| Saint Kitts and Nevis | Saint Lucia           | Saint Vincent and the Grenadines | Samoa                            |
| San Marino            | São Tomé and Príncipe | Senegal                          | Seychelles                       |
| Sierra Leone          | Solomon Islands       | Somalia                          | South Sudan                      |
| Sri Lanka             | Sudan                 | Suriname                         | Syria                            |
| Tajikistan            | Tanzania              | Timor-Leste                      | Togo                             |
| Tonga                 | Trinidad and Tobago   | Tunisia                          | Turkmenistan                     |
| Tuvalu                | Uganda                | Uruguay                          | Uzbekistan                       |
| Vanuatu               | Vatican City          | Yemen                            | Zambia                           |

--- 

### Contribution and Disputes

If you have any suggestions, disputes, or requests, please feel free to contact me. For any updates or changes related to the sovereign state list, please visit the [Wikipedia Talk Page](https://en.wikipedia.org/wiki/Talk:List_of_sovereign_states).

--- 

### Author

**Made by:** me :)
