# Insert_Endnote_format
###This program is useful when you have unconnected your paper with Endnote but you have to insert all the citations again.

####INPUT FILES  
My program can read `a Endnote library TXT file` containing all of the references which are already cited in your paper but in a plain text form.
You can get this file by:
Open Endnote->Select all the references in your endnote->File->Export->Save type: Text file & Output style: show all fields->Save

And the program also reads the already-cited `references list` in your paper or manuscript.  
For exmaple:
Tips: [Number][.][\t][Author_LastName1][Author_MiddleNameFirstName1][, OR & ][Author_LastName2]...[(][Year][)][Title][ ][Journal Name]...

1.	Karner MB, Delong EF, & Karl DM (2001) Archaeal dominance in the mesopelagic zone of the Pacific Ocean. Nature 409(6819):507-510.
2.	DeLong EF (1992) Archaea in coastal marine environments. Proc Natl Acad Sci U S A 89(12):5685-5689.
3.	Fuhrman JA, Mccallum K, & Davis AA (1992) Novel Major Archaebacterial Group from Marine Plankton. Nature 356(6365):148-149.
4.	Prosser JI & Nicol GW (2012) Archaeal and bacterial ammonia-oxidisers in soil: the quest for niche specialisation and differentiation. Trends in microbiology 20(11):523-531.
5.	Martens-Habbena W, Berube PM, Urakawa H, de la Torre JR, & Stahl DA (2009) Ammonia oxidation kinetics determine niche separation of nitrifying Archaea and Bacteria. Nature 461(7266):976-U234.
6.	Konneke M, et al. (2005) Isolation of an autotrophic ammonia-oxidizing marine archaeon. Nature 437(7058):543-546.
7.	Santoro AE, Richter RA, & Dupont CL (2019) Planktonic marine archaea. Annual review of marine science 11:131-158.
`Notice`: Your list must be in the style just like the below one or the programe won't recognize it (actually it is the PNAS format). 
But I will try to figure this out in the future.

###OUTPUT FILE  
And the programe will output the corresponding Endnote insert format you can paste directly into your paper:  
For example:
1. archaeal dominance in the meso|2001|Karner[Notice: This line is for checking]
1. {Karner, 2001 #26}[This is the Endnote Insert Format]
2. archaea in coastal marine envi|1992|DeLong
2. {DeLong, 1992 #15}
3. novel major archaebacterial gr|1992|Fuhrman
3. {Fuhrman, 1992 #18}
4. archaeal and bacterial ammonia|2012|Prosser
4. {Prosser, 2012 #49}
5. ammonia oxidation kinetics det|2009|Martens-Habbena
5. {Martens-Habbena, 2009 #42}
6. isolation of an autotrophic am|2005|Konneke
6. {Konneke, 2005 #33}
7. planktonic marine archaea|2019|Santoro
7. {Santoro, 2019 #424}
