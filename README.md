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

**When running the program, please run it again when you get the message:**
```
'tabulate' installed successfully. Please restart the program.
```

---

### Original Data Source
**World Population Review:** Began by sourcing information from [worldpopulationreview.com](https://worldpopulationreview.com), but it lacked data for certain countries, included non-country territories, and contained some inaccuracies. Only country codes and names were kept from this source. For these reasons, the data source was changed to Wikipedia due to its constant updates, as well as explanations and arguments supporting their decisions. 

*While the accuracy of Wikipedia is often questioned due to it being editable by anyone, contravercial pages such as ones used in this database are protected, meaning all changes and decisions need to be supported by proper evidence and support.*

---

### Deisions Made

- **Driving Side**: In cases where driving rules are different inside a country (e.g., overseas territories), the capital city's rules are used as the default.  
  **Example**:  
  - **United Kingdom**: Primarily left side, but some overseas territories, such as the British Indian Ocean Territory, drives on the right.

- **Minimum Licence Age**: This data is based on the [Wikipedia List of Minimum Driving Ages](https://en.wikipedia.org/wiki/List_of_minimum_driving_ages). The list shows the absolute minimum age to obtain any type of car licence (including learner's licences) in the **capital city** of each country.  
  **Example**:  
  - **Canada**: The minimum age to obtain a driver's licence is 16 in Ottawa (the capital), but is 14 in Alberta.

---

### Data Sources
- **ALPHA-2 CODE:** This data is based on the [IBAN Country Codes](https://www.iban.com/country-codes) website.  
- **Country List:** This list of sovereign is taken from  [Wikipedia's List of Sovereign states](https://en.wikipedia.org/wiki/List_of_sovereign_states#List_of_states).  
  - The "Other States" section was excluded for simplicity. 
  - The [Wikipedia talk page](https://en.wikipedia.org/wiki/Talk:List_of_sovereign_states) has all the details on the their reasoning of the inclusion of certain countries.
- **Driving Side:** This data is based on the [Wikipedia on Left- and Right-Hand Traffic](https://en.wikipedia.org/wiki/Left-_and_right-hand_traffic) page.
- **Minimum Licence Age:** This data is based on the [Wikipedia List of Minimum Driving Ages](https://en.wikipedia.org/wiki/List_of_minimum_driving_ages) page.
- **Alcohol Limit:** This data is based on the [Wikipedia Drunk driving law by country](https://en.wikipedia.org/wiki/Drunk_driving_law_by_country) page.
- **Max Speed:** This data is based on the [Wikipedia Speed Limits By Country](https://en.wikipedia.org/wiki/Speed_limits_by_country) page.

---

### Special Considerations
- Removed *The Republic of* and other prefixes for the sake of simplicity.
- **Ivory Coast**: Officially known as **Côte d'Ivoire**, but commonly referred to as Ivory Coast with English speakers.
- **Czech Republic**: Sometimes called **Czechia**.  
- **Democratic Republic of the Congo** and **Republic of the Congo**: Kepy the official names to avoid confusion between the two.  
- **Turkey**: Recemtly changed its name to **Türkiye**, but for ease of recognition, "Turkey" is used here.  
- **Cape Verde**: Officially known as **Cabo Verde**, but is more commonly known as **Cape Verde** with English speakers.  
- **Micronesia**: Officially **Federated States of Micronesia** but kept as simply **Micronesia** for convenience.

---

### Removed Countries
Territories that were excluded due to conflicts between data from **World Population Review** and **Wikipedia**. 

| Name | Reason |
| ------ | ----------- |
| Guadeloupe | French Territory. |
| Guam | US Territory. |
| Greenland | Danish Territory. |
| Hong Kong | Chinese Territory. |
| New Caledonia | French Territory. |
| Puerto Rico | US Territory. |
| Taiwan | Not included in the UN member states list on Wikipedia. |

---

### Added Countries

Many countries were added that were missing from **World Population Review**'s data. These countries are:  
- Afghanistan  
- Albania  
- Antigua and Barbuda  
- Armenia  
- Benin  
- Bhutan  
- Brunei  
- Burkina Faso  
- Burundi  
- Cape Verde  
- Central African Republic  
- Chad  
- Comoros  
- Cuba  
- Democratic Republic of the Congo  
- Djibouti  
- Equatorial Guinea  
- Eritrea  
- Eswatini  
- Ethiopia  
- Gambia  
- Grenada  
- Guinea  
- Guinea-Bissau  
- Guyana  
- Iran  
- Iraq  
- Ivory Coast  
- Kazakhstan  
- Kiribati  
- Kyrgyzstan  
- Liberia  
- Libya  
- Liechtenstein  
- Madagascar  
- Maldives  
- Marshall Islands  
- Mauritania  
- Micronesia  
- Monaco  
- Mongolia  
- Myanmar  
- Nauru  
- Nepal  
- Niger  
- North Korea  
- Palau  
- Palestine  
- Russia  
- Rwanda  
- Saint Kitts and Nevis  
- Saint Vincent and the Grenadines  
- San Marino  
- São Tomé and Príncipe  
- Sierra Leone  
- Solomon Islands  
- Somalia  
- South Sudan  
- Sudan  
- Suriname  
- Timor-Leste  
- Tonga  
- Turkmenistan  
- Tuvalu  
- United Arab Emirates  
- United States  
- Uzbekistan  
- Vatican City

---

### Contribution and Disputes

If you have any suggestions, disputes, or requests, please feel free to contact me. For any updates or changes related to the sovereign state list, please visit teh [Wikipedia Talk Page](https://en.wikipedia.org/wiki/Talk:List_of_sovereign_states).

--- 

### Author

**Made by:** me :)
