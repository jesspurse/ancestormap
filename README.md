# ancestormap
How I made my ancestor map

This was a long, long process that build off of work done by Ugluk4242 (https://github.com/Ugluk4242/GEDCOM_MAPPING, https://www.reddit.com/r/dataisbeautiful/comments/t8mw6z/oc_tracking_my_ancestors_migrations_with_400/?utm_source=share&utm_medium=web2x&context=3) and Yannick Brouwer (https://github.com/yannickbrouwer/ancestors-migration-visualization, https://yannickbrouwer.medium.com/visualizing-my-ancestry-on-a-map-7af6a2354db0)

1. I had never used Python before but have used SAS for years so there were some things that were easier for me to make in SAS.
2. I couldn't figure out Processing but maybe that would work for you.
3. Pandas datetime only goes from 1677-09-21 00:12:43.145224193 to 2262-04-11 23:47:16.854775807 which isn't super helpful for ancestry work.

I combined parts of both. First, I put my ancestors into myheritage.com and went back as far as I could possibly go based on verifiable records. Lots of census records, lots of wikipedia, trusting some other people's research.

THen I downloaded myheritage's app Family Tree Builder and synce my account to it. See fam_tree.png, fam_tree_export.png (choose birth and death), and fam_tree_csv.png.

Keep Gender, First Name, Last Name, Birth Date, Birth Place, Death Date, and Death Place.

I used Yannick's idea here to get the lat/long for each place: "Use the free plug-in Geocode by Awesome Tables (https://workspace.google.com/marketplace/app/geocode_by_awesome_table/904124517349) in Google Sheets to convert city names to latitude and longitude."

It mostly worked, but it helps to do some data cleaning on the places first. This is probably what took me the most time.

Then, you have one CSV file with birth year, birth lat and long, death year, and death lat and long. I just used Excel to make a per-year change (death lat - birth lat)/(death year - birth year) for lat and long for each person. If the person lived and died in the same place, the difference would be 0, but you'd still want that info so their dot appears on the map.

It's time for the SAS. This will go from one CSV with a line for each person to multiple CSVs - one for each year with everyone alive in that year and their location. See ancestorscsv.png and ancestors_942csv.png

Now, it's python time! Make sure cartopy is installed. First, you'll use creates_images. THen, you'll put creates_movie in the same folder as the images and run that - et voila, you'll have your ancestry map movie!
