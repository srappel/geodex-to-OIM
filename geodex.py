class GeodexDictionary:
    def __init__(self):
        """Create a new GeodexDictionary object"""
        self.map_type_dict = {
            30: "Administrative map",
            1: "Aerial photograph",
            6: "Aeronautical chart",
            7: "Bathymetric map",
            21: "Coal map",
            0 : "Not assigned",
            5 : "Geologic map",
            4 : "Hydrogeologic map",
            11 : "Land use map",
            12 : "Nautical chart",
            13 : "Orthophoto map",
            14 : "Planimetric map",
            998 : "Printed map - 2 color",
            997 : "Printed map - colored",
            996 : "Printed map - monochrome",
            995 : "Projection not indicated",
            15 : "Reference map",
            16 : "Road map",
            22 : "Satellite image map",
            24 : "Shaded relief map",
            18 : "Topo map (contours)",
            23 : "Topo map (form lines)",
            19 : "Topo map (hachures)",
            25 : "Topo map (irr interval)",
            20 : "Topo map (layer tints)"
        }

        self.production_dict = {
            38: "Blue line print",
            39: "Blueprint",
            37: "Negative microform",
            35: "Negative photocopy",
            34: "Positive photocopy",
            31: "Printed map - colored",
            33: "Printed map - monochrome",
            32: "Printed map - 2 color"
        }

        self.projection_dict = {
            0: "Not assigned",
            163 : "Azimuthal equidistant",
            185 : "Bonne",
            199 : "Cassini",
            182 : "Conic equidistant",
            183 : "Conic",
            171 : "Cylindrical",
            180 : "Gauss-Krüger",
            999 : "Gauss-Krüger",
            164 : "Gnomonic",
            186 : "Lambert conformal conic",
            175 : "Mercator",
            176 : "Miller",
            998 : "Munich PM",
            187 : "Polyconic",
            198 : "Polyhedric",
            161 : "Not indicated",
            178 : "Sinusoidal",
            168 : "Stereographic",
            179 : "Transverse Mercator"
        }

        self.primeMeridian_dict = {
            0 : "Not assigned",
            157 : "Athens PM",
            999 : "Cordoba PM",
            148 : "Copenhagen PM",
            135 : "Ferro PM",
            131 : "Greenwich PM",
            132 : "Madrid PM",
            146 : "Munich PM",
            142 : "Paris PM",
            138 : "Quito PM",
            147 : "Rome PM"
        }

        self.isoType_dict = {
            1 : "Isobars Feet",
            2 : "Isobars Fathoms",
            3 : "Isobars Meters",
            4 : "Contours Feet",
            5 : "Contours Meters",
            6 : "Multiple Isobar Types",
            7 : "No Isobar Indicated"
        }

        self.yearType_dict = { 
            97 : "Approximate Date", # datePub
            98 : "Publication Date", # datePub
            99 : "Compilation Date", # datePub
            100 : "Base Map Date", # date
            102 : "Field Checked", # dateSurvey
            103 : "Image Year", # datePhoto
            104 : "Photography to", # datePhoto
            105 : "Photo Inspected", # datePhoto
            106 : "Image Date", # datePhoto
            108 : "Preliminary Edition", # date
            109 : "Compiled From Map Dated", # datePSurvey
            110 : "Interim Edition", # date
            112 : "Printed", # datePub
            113 : "Printed Circa", # datePub
            114 : "Revised", # date
            115 : "Situation/Survey", # dateSurvey
            116 : "Transportation Network", # date
            118 : "Provisional Edition", # date
            120 : "Photo Revised", # datePhoto
            121 : "Edition of", # datePub
            119 : "Magnetic Declination Year" # date
        } 

class GeodexDates:
    def __init__(self, year1, year1_type, year2, year2_type, year3, year3_type, year4, year4_type):
        """Creates a new GeodexDate object"""
        self.year1 = year1
        self.year2 = year2        
        self.year3 = year3
        self.year4 = year4
        self.year1_type = year1_type
        self.year2_type = year2_type       
        self.year3_type = year3_type
        self.year4_type = year4_type

    def geodexDates2oimDates(self, input):
        oim_date_dict = {
            "datePub" : [97, 98, 99, 113, 121],
            "date" : [100, 110, 114, 116, 118, 119],
            "dateSurvey" : [102, 109, 115],
            "datePhoto" : [103, 104, 105, 106, 120],
            "dateReprint" : []
        }
        self.input = input
        self.datePub = None
        self.date = None
        self.dateSurvey = None
        self.datePhoto = None
        self.dateReprint = None

        if input in oim_date_dict["datePub"]


        return self.datePub, self.date, self.dateSurvey, self.datePhoto, self.dateReprint 