
CREATE TABLE `player_tiers` (
  `idplayer_tiers` int(11) NOT NULL AUTO_INCREMENT,
  `playerId` int(11) DEFAULT NULL,
  `playerDisplayName` varchar(45) DEFAULT NULL,
  `playerTier` int(11) DEFAULT NULL,
  `playerGroup` int(11) DEFAULT NULL,
  `uniqueId` varchar(45) DEFAULT NULL,
  `playerRealName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idplayer_tiers`)
) ENGINE=MyISAM AUTO_INCREMENT=200 DEFAULT CHARSET=latin1;
