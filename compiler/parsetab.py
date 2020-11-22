
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDORleftNOTleftLTLEGTGEEQNErightASSIGNleftSUMSUBleftMULDIVMODAND ASSIGN BOOLEAN COLON COMMA DIV ELSE ELSEIF EQ ERROR FALSE FLOAT FLOATNUMBER FOR FUNCTION GE GT ID IF IN INTEGER INTEGERNUMBER LCB LE LRB LSB LT MAIN MOD MUL NE NOT ON OR PRINT RCB RETURN RRB RSB SEMICOLON SUB SUM TRUE WHERE WHILEprogram : declist MAIN LRB RRB blockdeclist : declist dec\n    | epsdec : vardec\n    | funcdecvardec : idlist COLON type SEMICOLONfuncdec : FUNCTION ID LRB paramdecs RRB COLON type block\n    | FUNCTION ID LRB paramdecs RRB blocktype : INTEGER\n    | FLOAT\n    | BOOLEANiddec : lvalue\n    | ID ASSIGN exp\n    idlist : iddec\n    | idlist COMMA iddec\n    paramdecs : paramdecslist\n    | epsparamdecslist : paramdec\n    | paramdecslist COMMA paramdec\n    paramdec : ID COLON type\n    | ID LSB RSB COLON typeblock : LCB stmtlist RCBstmtlist : stmtlist stmt\n    | epslvalue : ID\n    | ID LSB exp RSBcase : WHERE const COLON stmtlistcases : cases case\n    | eps\n    stmt : ostmt\n    | cstmtostmt : IF LRB exp RRB simple\n    | IF LRB exp RRB ostmt\n    | IF LRB exp RRB cstmt elseiflist ELSE ostmt\n    | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB ostmt\n    | FOR LRB ID IN RRB ostmt\n    | WHILE LRB exp LRB ostmt\n    cstmt : simple\n    | IF LRB exp RRB cstmt elseiflist ELSE cstmt\n    | FOR LRB exp SEMICOLON exp SEMICOLON exp RRB cstmt\n    | FOR LRB ID IN RRB cstmt\n    | WHILE LRB exp LRB cstmt\n    elseiflist : elseiflist ELSEIF LRB exp RRB cstmt\n    | epssimple : RETURN exp SEMICOLON\n    | exp SEMICOLON\n    | block\n    | vardec\n    | ON LRB exp RRB LCB cases RCB SEMICOLON\n    | PRINT LRB ID RRB SEMICOLONrelop : GT\n    | GE\n    | LT\n    | LE\n    | EQ\n    | NEexp : lvalue ASSIGN exp\n    | exp operator exp %prec AND\n    | exp relop exp %prec LT\n    | const\n    | lvalue\n    | ID LRB explist RRB\n    | LRB exp RRB\n    | SUB exp\n    | NOT expoperator : AND\n    | OR\n    | SUM\n    | SUB\n    | MUL\n    | DIV\n    | MODconst : INTEGERNUMBER\n    | FLOATNUMBER\n    | TRUE\n    | FALSEexplist : exp\n    | explist COMMA exp\n    | epseps :'
    
_lr_action_items = {'MAIN':([0,2,3,5,6,7,40,80,99,121,],[-80,4,-3,-2,-4,-5,-6,-22,-8,-7,]),'FUNCTION':([0,2,3,5,6,7,40,80,99,121,],[-80,9,-3,-2,-4,-5,-6,-22,-8,-7,]),'ID':([0,2,3,5,6,7,9,15,17,18,25,30,31,32,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,67,68,72,80,81,82,83,86,90,91,92,99,102,103,104,105,106,108,109,117,121,122,123,125,128,129,132,133,134,136,139,140,141,144,150,151,152,153,154,157,158,159,160,161,166,167,168,173,174,176,179,181,182,184,],[-80,10,-3,-2,-4,-5,16,10,26,26,41,26,26,26,-80,-6,26,26,26,-66,-67,-68,-69,-70,-71,-72,-51,-52,-53,-54,-55,-56,26,88,-24,41,-22,-23,-30,-31,-38,26,-47,-48,-8,26,26,-46,115,26,26,119,-45,-7,88,26,88,-32,-33,88,-37,-42,-50,26,-36,-41,88,-39,-34,26,88,-49,-35,-40,-80,88,88,26,171,26,88,26,88,88,26,88,88,]),'$end':([1,38,80,],[0,-1,-22,]),'LRB':([4,16,17,18,26,28,29,30,31,32,33,34,35,36,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,64,65,66,67,68,76,77,78,79,80,81,82,83,84,86,87,88,89,90,91,92,93,94,101,102,103,104,105,106,108,115,116,117,122,123,125,128,129,132,133,134,136,139,140,141,144,145,150,151,152,153,154,157,158,159,160,161,163,164,165,166,167,168,171,172,173,174,176,179,181,182,184,],[13,25,30,30,46,-61,-60,30,30,30,-73,-74,-75,-76,-80,-6,30,30,30,-66,-67,-68,-69,-70,-71,-72,-51,-52,-53,-54,-55,-56,30,-64,-65,-26,30,-24,-58,-59,-57,-63,-22,-23,-30,-31,103,-38,105,46,106,30,-47,-48,108,109,-62,30,30,-46,30,30,30,46,125,-45,30,30,30,-32,-33,30,-37,-42,-50,30,-36,-41,30,152,-39,-34,30,30,-49,-35,-40,-80,30,30,166,167,168,30,30,30,46,176,30,30,30,30,30,30,30,]),'COLON':([8,10,11,12,24,26,27,28,29,33,34,35,36,41,64,65,66,71,76,77,78,79,88,95,97,101,155,],[14,-25,-14,-12,-15,-25,-13,-61,-60,-73,-74,-75,-76,69,-64,-65,-26,98,-58,-59,-57,-63,-25,-12,110,-62,159,]),'COMMA':([8,10,11,12,21,22,23,24,26,27,28,29,33,34,35,36,43,45,46,64,65,66,73,74,75,76,77,78,79,88,95,96,100,101,112,120,],[15,-25,-14,-12,-9,-10,-11,-15,-25,-13,-61,-60,-73,-74,-75,-76,72,-18,-80,-64,-65,-26,102,-77,-79,-58,-59,-57,-63,-25,-12,-20,-19,-62,-78,-21,]),'ASSIGN':([10,26,28,66,88,95,115,171,],[17,-25,62,-26,17,62,-25,-25,]),'LSB':([10,26,41,88,115,171,],[18,18,70,18,18,18,]),'RRB':([13,21,22,23,25,26,28,29,33,34,35,36,42,43,44,45,46,63,64,65,66,73,74,75,76,77,78,79,96,100,101,112,113,118,119,120,124,146,156,169,175,183,],[19,-9,-10,-11,-80,-25,-61,-60,-73,-74,-75,-76,71,-16,-17,-18,-80,79,-64,-65,-26,101,-77,-79,-58,-59,-57,-63,-20,-19,-62,-78,122,126,127,-21,132,153,160,173,179,184,]),'INTEGER':([14,69,98,110,],[21,21,21,21,]),'FLOAT':([14,69,98,110,],[22,22,22,22,]),'BOOLEAN':([14,69,98,110,],[23,23,23,23,]),'SUB':([17,18,26,27,28,29,30,31,32,33,34,35,36,37,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,74,76,77,78,79,80,81,82,83,85,86,88,90,91,92,95,101,102,103,104,105,106,107,108,112,113,114,115,116,117,118,122,123,125,128,129,131,132,133,134,136,139,140,141,144,146,150,151,152,153,154,156,157,158,159,160,161,166,167,168,169,170,171,172,173,174,176,178,179,181,182,183,184,],[31,31,-25,52,-61,-60,31,31,31,-73,-74,-75,-76,52,-80,-6,31,31,31,-66,-67,-68,-69,-70,-71,-72,-51,-52,-53,-54,-55,-56,31,52,-64,52,-26,31,-24,52,52,52,52,-63,-22,-23,-30,-31,52,-38,-25,31,-47,-48,-61,-62,31,31,-46,31,31,52,31,52,52,52,-25,52,-45,52,31,31,31,-32,-33,52,31,-37,-42,-50,31,-36,-41,31,52,-39,-34,31,31,-49,52,-35,-40,-80,31,31,31,31,31,52,52,-25,52,31,31,31,52,31,31,31,52,31,]),'NOT':([17,18,30,31,32,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,67,68,80,81,82,83,86,90,91,92,102,103,104,105,106,108,117,122,123,125,128,129,132,133,134,136,139,140,141,144,150,151,152,153,154,157,158,159,160,161,166,167,168,173,174,176,179,181,182,184,],[32,32,32,32,32,-80,-6,32,32,32,-66,-67,-68,-69,-70,-71,-72,-51,-52,-53,-54,-55,-56,32,32,-24,-22,-23,-30,-31,-38,32,-47,-48,32,32,-46,32,32,32,-45,32,32,32,-32,-33,32,-37,-42,-50,32,-36,-41,32,-39,-34,32,32,-49,-35,-40,-80,32,32,32,32,32,32,32,32,32,32,32,32,]),'INTEGERNUMBER':([17,18,30,31,32,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,67,68,80,81,82,83,86,90,91,92,102,103,104,105,106,108,117,122,123,125,128,129,132,133,134,136,139,140,141,144,149,150,151,152,153,154,157,158,159,160,161,166,167,168,173,174,176,179,181,182,184,],[33,33,33,33,33,-80,-6,33,33,33,-66,-67,-68,-69,-70,-71,-72,-51,-52,-53,-54,-55,-56,33,33,-24,-22,-23,-30,-31,-38,33,-47,-48,33,33,-46,33,33,33,-45,33,33,33,-32,-33,33,-37,-42,-50,33,-36,-41,33,33,-39,-34,33,33,-49,-35,-40,-80,33,33,33,33,33,33,33,33,33,33,33,33,]),'FLOATNUMBER':([17,18,30,31,32,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,67,68,80,81,82,83,86,90,91,92,102,103,104,105,106,108,117,122,123,125,128,129,132,133,134,136,139,140,141,144,149,150,151,152,153,154,157,158,159,160,161,166,167,168,173,174,176,179,181,182,184,],[34,34,34,34,34,-80,-6,34,34,34,-66,-67,-68,-69,-70,-71,-72,-51,-52,-53,-54,-55,-56,34,34,-24,-22,-23,-30,-31,-38,34,-47,-48,34,34,-46,34,34,34,-45,34,34,34,-32,-33,34,-37,-42,-50,34,-36,-41,34,34,-39,-34,34,34,-49,-35,-40,-80,34,34,34,34,34,34,34,34,34,34,34,34,]),'TRUE':([17,18,30,31,32,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,67,68,80,81,82,83,86,90,91,92,102,103,104,105,106,108,117,122,123,125,128,129,132,133,134,136,139,140,141,144,149,150,151,152,153,154,157,158,159,160,161,166,167,168,173,174,176,179,181,182,184,],[35,35,35,35,35,-80,-6,35,35,35,-66,-67,-68,-69,-70,-71,-72,-51,-52,-53,-54,-55,-56,35,35,-24,-22,-23,-30,-31,-38,35,-47,-48,35,35,-46,35,35,35,-45,35,35,35,-32,-33,35,-37,-42,-50,35,-36,-41,35,35,-39,-34,35,35,-49,-35,-40,-80,35,35,35,35,35,35,35,35,35,35,35,35,]),'FALSE':([17,18,30,31,32,39,40,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,67,68,80,81,82,83,86,90,91,92,102,103,104,105,106,108,117,122,123,125,128,129,132,133,134,136,139,140,141,144,149,150,151,152,153,154,157,158,159,160,161,166,167,168,173,174,176,179,181,182,184,],[36,36,36,36,36,-80,-6,36,36,36,-66,-67,-68,-69,-70,-71,-72,-51,-52,-53,-54,-55,-56,36,36,-24,-22,-23,-30,-31,-38,36,-47,-48,36,36,-46,36,36,36,-45,36,36,36,-32,-33,36,-37,-42,-50,36,-36,-41,36,36,-39,-34,36,36,-49,-35,-40,-80,36,36,36,36,36,36,36,36,36,36,36,36,]),'LCB':([19,21,22,23,39,40,67,68,71,80,81,82,83,86,91,92,104,111,117,122,125,126,128,129,132,133,134,136,140,141,144,150,151,153,154,157,158,159,160,161,173,176,179,182,184,],[39,-9,-10,-11,-80,-6,39,-24,39,-22,-23,-30,-31,-38,-47,-48,-46,39,-45,39,39,135,-32,-33,39,-37,-42,-50,-36,-41,39,-39,-34,39,-49,-35,-40,-80,39,39,39,39,39,39,39,]),'SEMICOLON':([20,21,22,23,26,28,29,33,34,35,36,64,65,66,76,77,78,79,85,88,95,101,107,114,115,127,131,147,170,171,178,],[40,-9,-10,-11,-25,-61,-60,-73,-74,-75,-76,-64,-65,-26,-58,-59,-57,-63,104,-25,-61,-62,117,123,-25,136,139,154,174,-25,181,]),'AND':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,49,-61,-60,-73,-74,-75,-76,49,49,-64,-65,-26,49,-58,-59,-57,-63,49,-25,-61,-62,49,49,49,49,-25,49,49,49,49,49,49,49,-25,49,49,49,]),'OR':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,50,-61,-60,-73,-74,-75,-76,50,50,-64,-65,-26,50,-58,-59,-57,-63,50,-25,-61,-62,50,50,50,50,-25,50,50,50,50,50,50,50,-25,50,50,50,]),'SUM':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,51,-61,-60,-73,-74,-75,-76,51,51,-64,51,-26,51,51,51,51,-63,51,-25,-61,-62,51,51,51,51,-25,51,51,51,51,51,51,51,-25,51,51,51,]),'MUL':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,53,-61,-60,-73,-74,-75,-76,53,53,53,53,-26,53,53,53,53,-63,53,-25,-61,-62,53,53,53,53,-25,53,53,53,53,53,53,53,-25,53,53,53,]),'DIV':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,54,-61,-60,-73,-74,-75,-76,54,54,54,54,-26,54,54,54,54,-63,54,-25,-61,-62,54,54,54,54,-25,54,54,54,54,54,54,54,-25,54,54,54,]),'MOD':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,55,-61,-60,-73,-74,-75,-76,55,55,55,55,-26,55,55,55,55,-63,55,-25,-61,-62,55,55,55,55,-25,55,55,55,55,55,55,55,-25,55,55,55,]),'GT':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,56,-61,-60,-73,-74,-75,-76,56,56,-64,56,-26,56,56,-59,-57,-63,56,-25,-61,-62,56,56,56,56,-25,56,56,56,56,56,56,56,-25,56,56,56,]),'GE':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,57,-61,-60,-73,-74,-75,-76,57,57,-64,57,-26,57,57,-59,-57,-63,57,-25,-61,-62,57,57,57,57,-25,57,57,57,57,57,57,57,-25,57,57,57,]),'LT':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,58,-61,-60,-73,-74,-75,-76,58,58,-64,58,-26,58,58,-59,-57,-63,58,-25,-61,-62,58,58,58,58,-25,58,58,58,58,58,58,58,-25,58,58,58,]),'LE':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,59,-61,-60,-73,-74,-75,-76,59,59,-64,59,-26,59,59,-59,-57,-63,59,-25,-61,-62,59,59,59,59,-25,59,59,59,59,59,59,59,-25,59,59,59,]),'EQ':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,60,-61,-60,-73,-74,-75,-76,60,60,-64,60,-26,60,60,-59,-57,-63,60,-25,-61,-62,60,60,60,60,-25,60,60,60,60,60,60,60,-25,60,60,60,]),'NE':([26,27,28,29,33,34,35,36,37,63,64,65,66,74,76,77,78,79,85,88,95,101,107,112,113,114,115,116,118,131,146,156,169,170,171,172,178,183,],[-25,61,-61,-60,-73,-74,-75,-76,61,61,-64,61,-26,61,61,-59,-57,-63,61,-25,-61,-62,61,61,61,61,-25,61,61,61,61,61,61,61,-25,61,61,61,]),'RSB':([26,28,29,33,34,35,36,37,64,65,66,70,76,77,78,79,101,],[-25,-61,-60,-73,-74,-75,-76,66,-64,-65,-26,97,-58,-59,-57,-63,-62,]),'RCB':([39,40,67,68,80,81,82,83,86,91,92,104,117,128,129,133,134,135,136,140,141,142,143,148,150,151,154,157,158,159,161,],[-80,-6,80,-24,-22,-23,-30,-31,-38,-47,-48,-46,-45,-32,-33,-37,-42,-80,-50,-36,-41,147,-29,-28,-39,-34,-49,-35,-40,-80,-27,]),'IF':([39,40,67,68,80,81,82,83,86,91,92,104,117,122,125,128,129,132,133,134,136,140,141,144,150,151,153,154,157,158,159,160,161,173,176,179,182,184,],[-80,-6,84,-24,-22,-23,-30,-31,-38,-47,-48,-46,-45,84,84,-32,-33,84,-37,-42,-50,-36,-41,84,-39,-34,84,-49,-35,-40,-80,163,84,163,163,163,163,163,]),'FOR':([39,40,67,68,80,81,82,83,86,91,92,104,117,122,125,128,129,132,133,134,136,140,141,144,150,151,153,154,157,158,159,160,161,173,176,179,182,184,],[-80,-6,87,-24,-22,-23,-30,-31,-38,-47,-48,-46,-45,87,87,-32,-33,87,-37,-42,-50,-36,-41,87,-39,-34,87,-49,-35,-40,-80,164,87,164,164,164,164,164,]),'WHILE':([39,40,67,68,80,81,82,83,86,91,92,104,117,122,125,128,129,132,133,134,136,140,141,144,150,151,153,154,157,158,159,160,161,173,176,179,182,184,],[-80,-6,89,-24,-22,-23,-30,-31,-38,-47,-48,-46,-45,89,89,-32,-33,89,-37,-42,-50,-36,-41,89,-39,-34,89,-49,-35,-40,-80,165,89,165,165,165,165,165,]),'RETURN':([39,40,67,68,80,81,82,83,86,91,92,104,117,122,125,128,129,132,133,134,136,140,141,144,150,151,153,154,157,158,159,160,161,173,176,179,182,184,],[-80,-6,90,-24,-22,-23,-30,-31,-38,-47,-48,-46,-45,90,90,-32,-33,90,-37,-42,-50,-36,-41,90,-39,-34,90,-49,-35,-40,-80,90,90,90,90,90,90,90,]),'ON':([39,40,67,68,80,81,82,83,86,91,92,104,117,122,125,128,129,132,133,134,136,140,141,144,150,151,153,154,157,158,159,160,161,173,176,179,182,184,],[-80,-6,93,-24,-22,-23,-30,-31,-38,-47,-48,-46,-45,93,93,-32,-33,93,-37,-42,-50,-36,-41,93,-39,-34,93,-49,-35,-40,-80,93,93,93,93,93,93,93,]),'PRINT':([39,40,67,68,80,81,82,83,86,91,92,104,117,122,125,128,129,132,133,134,136,140,141,144,150,151,153,154,157,158,159,160,161,173,176,179,182,184,],[-80,-6,94,-24,-22,-23,-30,-31,-38,-47,-48,-46,-45,94,94,-32,-33,94,-37,-42,-50,-36,-41,94,-39,-34,94,-49,-35,-40,-80,94,94,94,94,94,94,94,]),'WHERE':([40,68,80,81,82,83,86,91,92,104,117,128,129,133,134,135,136,140,141,142,143,148,150,151,154,157,158,159,161,],[-6,-24,-22,-23,-30,-31,-38,-47,-48,-46,-45,-32,-33,-37,-42,-80,-50,-36,-41,149,-29,-28,-39,-34,-49,-35,-40,-80,-27,]),'ELSE':([40,80,86,91,92,104,117,128,130,134,136,137,138,141,150,154,158,162,177,180,],[-6,-22,-38,-47,-48,-46,-45,-38,-80,-42,-50,144,-44,-41,-39,-49,-40,-43,-80,182,]),'ELSEIF':([40,80,86,91,92,104,117,128,130,134,136,137,138,141,150,154,158,162,177,180,],[-6,-22,-38,-47,-48,-46,-45,-38,-80,-42,-50,145,-44,-41,-39,-49,-40,-43,-80,145,]),'IN':([115,171,],[124,175,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,],[2,]),'eps':([0,25,39,46,130,135,159,177,],[3,44,68,75,138,143,68,138,]),'dec':([2,],[5,]),'vardec':([2,67,122,125,132,144,153,160,161,173,176,179,182,184,],[6,92,92,92,92,92,92,92,92,92,92,92,92,92,]),'funcdec':([2,],[7,]),'idlist':([2,67,122,125,132,144,153,160,161,173,176,179,182,184,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'iddec':([2,15,67,122,125,132,144,153,160,161,173,176,179,182,184,],[11,24,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'lvalue':([2,15,17,18,30,31,32,46,47,48,62,67,90,102,103,105,106,108,122,123,125,132,139,144,152,153,160,161,166,167,168,173,174,176,179,181,182,184,],[12,12,28,28,28,28,28,28,28,28,28,95,28,28,28,28,28,28,95,28,95,95,28,95,28,95,95,95,28,28,28,95,28,95,95,28,95,95,]),'type':([14,69,98,110,],[20,96,111,120,]),'exp':([17,18,30,31,32,46,47,48,62,67,90,102,103,105,106,108,122,123,125,132,139,144,152,153,160,161,166,167,168,173,174,176,179,181,182,184,],[27,37,63,64,65,74,76,77,78,85,107,112,113,114,116,118,85,131,85,85,146,85,156,85,85,85,169,170,172,85,178,85,85,183,85,85,]),'const':([17,18,30,31,32,46,47,48,62,67,90,102,103,105,106,108,122,123,125,132,139,144,149,152,153,160,161,166,167,168,173,174,176,179,181,182,184,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,155,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'block':([19,67,71,111,122,125,132,144,153,160,161,173,176,179,182,184,],[38,91,99,121,91,91,91,91,91,91,91,91,91,91,91,91,]),'paramdecs':([25,],[42,]),'paramdecslist':([25,],[43,]),'paramdec':([25,72,],[45,100,]),'operator':([27,37,63,64,65,74,76,77,78,85,107,112,113,114,116,118,131,146,156,169,170,172,178,183,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'relop':([27,37,63,64,65,74,76,77,78,85,107,112,113,114,116,118,131,146,156,169,170,172,178,183,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'stmtlist':([39,159,],[67,161,]),'explist':([46,],[73,]),'stmt':([67,161,],[81,81,]),'ostmt':([67,122,125,132,144,153,161,],[82,129,133,140,151,157,82,]),'cstmt':([67,122,125,132,144,153,160,161,173,176,179,182,184,],[83,130,134,141,150,158,162,83,177,134,141,150,158,]),'simple':([67,122,125,132,144,153,160,161,173,176,179,182,184,],[86,128,86,86,86,86,86,86,86,86,86,86,86,]),'elseiflist':([130,177,],[137,180,]),'cases':([135,],[142,]),'case':([142,],[148,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist MAIN LRB RRB block','program',5,'p_program','parser.py',15),
  ('declist -> declist dec','declist',2,'p_declist','parser.py',20),
  ('declist -> eps','declist',1,'p_declist','parser.py',21),
  ('dec -> vardec','dec',1,'p_dec','parser.py',27),
  ('dec -> funcdec','dec',1,'p_dec','parser.py',28),
  ('vardec -> idlist COLON type SEMICOLON','vardec',4,'p_vardec','parser.py',33),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB COLON type block','funcdec',8,'p_funcdec','parser.py',38),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB block','funcdec',6,'p_funcdec','parser.py',39),
  ('type -> INTEGER','type',1,'p_type','parser.py',44),
  ('type -> FLOAT','type',1,'p_type','parser.py',45),
  ('type -> BOOLEAN','type',1,'p_type','parser.py',46),
  ('iddec -> lvalue','iddec',1,'p_iddec','parser.py',51),
  ('iddec -> ID ASSIGN exp','iddec',3,'p_iddec','parser.py',52),
  ('idlist -> iddec','idlist',1,'p_idlist','parser.py',58),
  ('idlist -> idlist COMMA iddec','idlist',3,'p_idlist','parser.py',59),
  ('paramdecs -> paramdecslist','paramdecs',1,'p_paramdecs','parser.py',65),
  ('paramdecs -> eps','paramdecs',1,'p_paramdecs','parser.py',66),
  ('paramdecslist -> paramdec','paramdecslist',1,'p_paramdecslist','parser.py',71),
  ('paramdecslist -> paramdecslist COMMA paramdec','paramdecslist',3,'p_paramdecslist','parser.py',72),
  ('paramdec -> ID COLON type','paramdec',3,'p_paramdec','parser.py',78),
  ('paramdec -> ID LSB RSB COLON type','paramdec',5,'p_paramdec','parser.py',79),
  ('block -> LCB stmtlist RCB','block',3,'p_block','parser.py',84),
  ('stmtlist -> stmtlist stmt','stmtlist',2,'p_stmtlist','parser.py',89),
  ('stmtlist -> eps','stmtlist',1,'p_stmtlist','parser.py',90),
  ('lvalue -> ID','lvalue',1,'p_lvalue','parser.py',95),
  ('lvalue -> ID LSB exp RSB','lvalue',4,'p_lvalue','parser.py',96),
  ('case -> WHERE const COLON stmtlist','case',4,'p_case','parser.py',101),
  ('cases -> cases case','cases',2,'p_cases','parser.py',106),
  ('cases -> eps','cases',1,'p_cases','parser.py',107),
  ('stmt -> ostmt','stmt',1,'p_stmt','parser.py',113),
  ('stmt -> cstmt','stmt',1,'p_stmt','parser.py',114),
  ('ostmt -> IF LRB exp RRB simple','ostmt',5,'p_ostmt','parser.py',119),
  ('ostmt -> IF LRB exp RRB ostmt','ostmt',5,'p_ostmt','parser.py',120),
  ('ostmt -> IF LRB exp RRB cstmt elseiflist ELSE ostmt','ostmt',8,'p_ostmt','parser.py',121),
  ('ostmt -> FOR LRB exp SEMICOLON exp SEMICOLON exp RRB ostmt','ostmt',9,'p_ostmt','parser.py',122),
  ('ostmt -> FOR LRB ID IN RRB ostmt','ostmt',6,'p_ostmt','parser.py',123),
  ('ostmt -> WHILE LRB exp LRB ostmt','ostmt',5,'p_ostmt','parser.py',124),
  ('cstmt -> simple','cstmt',1,'p_cstmt','parser.py',129),
  ('cstmt -> IF LRB exp RRB cstmt elseiflist ELSE cstmt','cstmt',8,'p_cstmt','parser.py',130),
  ('cstmt -> FOR LRB exp SEMICOLON exp SEMICOLON exp RRB cstmt','cstmt',9,'p_cstmt','parser.py',131),
  ('cstmt -> FOR LRB ID IN RRB cstmt','cstmt',6,'p_cstmt','parser.py',132),
  ('cstmt -> WHILE LRB exp LRB cstmt','cstmt',5,'p_cstmt','parser.py',133),
  ('elseiflist -> elseiflist ELSEIF LRB exp RRB cstmt','elseiflist',6,'p_elseiflist','parser.py',138),
  ('elseiflist -> eps','elseiflist',1,'p_elseiflist','parser.py',139),
  ('simple -> RETURN exp SEMICOLON','simple',3,'p_simple','parser.py',144),
  ('simple -> exp SEMICOLON','simple',2,'p_simple','parser.py',145),
  ('simple -> block','simple',1,'p_simple','parser.py',146),
  ('simple -> vardec','simple',1,'p_simple','parser.py',147),
  ('simple -> ON LRB exp RRB LCB cases RCB SEMICOLON','simple',8,'p_simple','parser.py',148),
  ('simple -> PRINT LRB ID RRB SEMICOLON','simple',5,'p_simple','parser.py',149),
  ('relop -> GT','relop',1,'p_relop','parser.py',154),
  ('relop -> GE','relop',1,'p_relop','parser.py',155),
  ('relop -> LT','relop',1,'p_relop','parser.py',156),
  ('relop -> LE','relop',1,'p_relop','parser.py',157),
  ('relop -> EQ','relop',1,'p_relop','parser.py',158),
  ('relop -> NE','relop',1,'p_relop','parser.py',159),
  ('exp -> lvalue ASSIGN exp','exp',3,'p_exp','parser.py',164),
  ('exp -> exp operator exp','exp',3,'p_exp','parser.py',165),
  ('exp -> exp relop exp','exp',3,'p_exp','parser.py',166),
  ('exp -> const','exp',1,'p_exp','parser.py',167),
  ('exp -> lvalue','exp',1,'p_exp','parser.py',168),
  ('exp -> ID LRB explist RRB','exp',4,'p_exp','parser.py',169),
  ('exp -> LRB exp RRB','exp',3,'p_exp','parser.py',170),
  ('exp -> SUB exp','exp',2,'p_exp','parser.py',171),
  ('exp -> NOT exp','exp',2,'p_exp','parser.py',172),
  ('operator -> AND','operator',1,'p_operator','parser.py',177),
  ('operator -> OR','operator',1,'p_operator','parser.py',178),
  ('operator -> SUM','operator',1,'p_operator','parser.py',179),
  ('operator -> SUB','operator',1,'p_operator','parser.py',180),
  ('operator -> MUL','operator',1,'p_operator','parser.py',181),
  ('operator -> DIV','operator',1,'p_operator','parser.py',182),
  ('operator -> MOD','operator',1,'p_operator','parser.py',183),
  ('const -> INTEGERNUMBER','const',1,'p_const','parser.py',188),
  ('const -> FLOATNUMBER','const',1,'p_const','parser.py',189),
  ('const -> TRUE','const',1,'p_const','parser.py',190),
  ('const -> FALSE','const',1,'p_const','parser.py',191),
  ('explist -> exp','explist',1,'p_explist','parser.py',196),
  ('explist -> explist COMMA exp','explist',3,'p_explist','parser.py',197),
  ('explist -> eps','explist',1,'p_explist','parser.py',198),
  ('eps -> <empty>','eps',0,'p_eps','parser.py',203),
]
