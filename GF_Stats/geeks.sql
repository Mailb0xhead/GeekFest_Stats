CREATE TABLE `geeks` (
  `idGeek` int(11) NOT NULL AUTO_INCREMENT,
  `handle` varchar(45) DEFAULT NULL,
  `firstname` varchar(45) DEFAULT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `occupation` varchar(45) DEFAULT NULL,
  `memberSince` datetime DEFAULT NULL,
  `attendingGF2018` varchar(5) DEFAULT NULL,
  `CSGO` varchar(5) DEFAULT NULL,
  `BF3` varchar(5) DEFAULT NULL,
  `uniqueId` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idGeek`)
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
