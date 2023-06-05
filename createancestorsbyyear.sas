/* creates library*/
libname ancestry '/path/';

/* imports your ancestors file */
proc import datafile="/path/ancestors.csv"
dbms=csv
out=ancestry.people
replace;
run;

/* this creates a line per year for each person. */
data ancestry.create;
set ancestry.people;
do until (year = finalyear);
year = year + 1;
mlat = mlat + latdiff;
mlon = mlon + londiff;
output;
end;
drop latdiff londiff finalyear yeardiff;
run;

/* this exports the full dataset as a csv */
proc export data=ancestry.create
dbms = csv
outfile = "/home/jpurser0/ancestors_allyears.csv"
replace;
run;

/* this creates a csv file for EACH year with lines for each person who existed in that year */
/* change path to wherever you want it to go PLUS the start of the name you want to use in the csv */
data _null_;
  set ancestry.comp_all;
  length fv $ 200;
if year<1000 then do;
  fv = "/path/ancestors_" || TRIM(put(year,3.)) || ".csv";
  end;
else if year>=1000 then do;
  fv = "/path/ancestors_" || TRIM(put(year,4.)) || ".csv";
  end;
  file write filevar=fv dsd dlm=',' lrecl=32000 ;
  put (_all_) (:);
run;
