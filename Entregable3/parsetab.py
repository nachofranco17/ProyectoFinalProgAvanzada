
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'statementleftANDORnonassocBETWEENIGUALMAYOR_QUEMENOR_QUEMAYOR_IGUALMENOR_IGUALDIFERENTEACTUALIZA ADD_COLUMN AGREGA_LA_COLUMNA AGRUPANDO_POR ALTER_TABLE AND ASTERISCO AVG BETWEEN BORRA_DE_LA CAMBIA_LA_TABLA CAST CLAVE_PRIMA CLAVE_REFERENTE COMA COMO_MUCHO CONTANDO COUNT CREATE_TABLE CREA_LA_TABLA DEFAULT DELETE_FROM DE_LA_TABLA DIFERENTE DISTINCT DONDE DROP_COLUMN DROP_TABLE ELIMINA_LA_COLUMNA EN ENTRE EN_ESTO ES_NULO EXISTE EXISTS FLOAT FOREIGN_KEY FROM GROUP_BY HAVING ID IGUAL IN INSERT_INTO INT IS_NULL JOIN LIKE LIMIT LOS_DISTINTOS LOS_VALORES MAX MAYOR_IGUAL MAYOR_QUE MENOR_IGUAL MENOR_QUE METE_EN MEZCLANDO MIN NOT_NULL NO_NULO NUM ON OR ORDENA_POR ORDER_BY PARECIDO_A PARENDER PARENIZQ POR_DEFECTO PRIMARY_KEY PUNTO PUNTO_Y_COMA SELECT SET SETEA STRING SUM TIRA_LA_TABLA TODO TRAEME TRANSFORMA_A UNICO UNIQUE UPDATE VALUES VARCHAR WHERE WHERE_DEL_GROUP_BY Ystatement : select_statement\n                 | insert_statement\n                 | update_statement\n                 | delete_statement\n                 | alter_table_statementselect_statement : SELECT opt_distinct select_list FROM table_list opt_join_clause opt_where_clause opt_group_by_clause opt_having_clause opt_order_by_clause PUNTO_Y_COMAopt_order_by_clause : ORDER_BY column_list\n                           | emptyopt_distinct : DISTINCT\n                    | emptyselect_list : ASTERISCO\n                   | select_itemsselect_items : select_items COMA select_item\n                    | select_itemselect_item : DISTINCT identifier\n                   | identifier\n                   | function_callfunction_call : COUNT PARENIZQ operand PARENDER\n                     | SUM PARENIZQ operand PARENDER\n                     | AVG PARENIZQ operand PARENDER\n                     | MIN PARENIZQ operand PARENDER\n                     | MAX PARENIZQ operand PARENDERcolumn_list : identifier\n                   | identifier COMA column_listtable_list : identifier\n                  | identifier COMA table_listopt_join_clause : JOIN identifier ON condition\n                       | emptyopt_where_clause : WHERE condition\n                        | emptyopt_group_by_clause : GROUP_BY column_list\n                           | emptyopt_having_clause : HAVING condition\n                         | emptycondition : expression\n                 | condition AND condition\n                 | condition OR conditionoperand : value\n               | aggregate_functionvalue : NUM\n             | STRING\n             | identifier\n             | ASTERISCOexpression : operand comparador operand\n                  | operand BETWEEN operand AND operandaggregate_function : COUNT PARENIZQ operand PARENDER\n                          | SUM PARENIZQ operand PARENDER\n                          | AVG PARENIZQ operand PARENDER\n                          | MIN PARENIZQ operand PARENDER\n                          | MAX PARENIZQ operand PARENDERcomparador : IGUAL\n                  | MAYOR_QUE\n                  | MENOR_QUE\n                  | MAYOR_IGUAL\n                  | MENOR_IGUAL\n                  | DIFERENTEinsert_statement : INSERT_INTO identifier PARENIZQ column_list PARENDER VALUES PARENIZQ value_list PARENDER PUNTO_Y_COMAvalue_list : value\n                  | value COMA value_listupdate_statement : UPDATE identifier SET assignment_list opt_where_clause PUNTO_Y_COMAassignment_list : assignment\n                       | assignment COMA assignment_listassignment : identifier IGUAL valuedelete_statement : DELETE_FROM identifier opt_where_clause PUNTO_Y_COMAalter_table_statement : ALTER_TABLE identifier ADD_COLUMN column_definition PUNTO_Y_COMA\n                             | ALTER_TABLE identifier DROP_COLUMN identifier PUNTO_Y_COMAcolumn_definition : identifier data_type column_constraintsdata_type : VARCHAR PARENIZQ NUM PARENDER\n                 | INTcolumn_constraints : constraint\n                          | column_constraints constraintconstraint : NOT_NULL\n                  | UNIQUE\n                  | PRIMARY_KEY\n                  | FOREIGN_KEYidentifier : ID\n                  | ID PUNTO IDempty :'
    
_lr_action_items = {'SELECT':([0,],[7,]),'INSERT_INTO':([0,],[8,]),'UPDATE':([0,],[9,]),'DELETE_FROM':([0,],[10,]),'ALTER_TABLE':([0,],[11,]),'$end':([1,2,3,4,5,6,54,103,104,117,166,168,],[0,-1,-2,-3,-4,-5,-64,-65,-66,-60,-57,-6,]),'DISTINCT':([7,12,13,14,41,],[13,24,-9,-10,24,]),'ASTERISCO':([7,12,13,14,36,43,44,45,46,47,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,138,139,150,156,161,],[-78,21,-9,-10,63,63,63,63,63,63,63,63,63,63,63,-51,-52,-53,-54,-55,-56,63,63,63,63,63,63,63,63,63,63,]),'ID':([7,8,9,10,11,12,13,14,24,32,33,34,36,38,39,40,41,43,44,45,46,47,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,106,108,138,139,148,150,156,161,163,],[-78,16,16,16,16,16,-9,-10,16,16,50,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-51,-52,-53,-54,-55,-56,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'COUNT':([7,12,13,14,36,41,43,44,45,46,47,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,139,150,156,],[-78,27,-9,-10,64,27,64,64,64,64,64,64,64,64,64,-51,-52,-53,-54,-55,-56,64,64,64,64,64,64,64,64,]),'SUM':([7,12,13,14,36,41,43,44,45,46,47,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,139,150,156,],[-78,28,-9,-10,65,28,65,65,65,65,65,65,65,65,65,-51,-52,-53,-54,-55,-56,65,65,65,65,65,65,65,65,]),'AVG':([7,12,13,14,36,41,43,44,45,46,47,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,139,150,156,],[-78,29,-9,-10,66,29,66,66,66,66,66,66,66,66,66,-51,-52,-53,-54,-55,-56,66,66,66,66,66,66,66,66,]),'MIN':([7,12,13,14,36,41,43,44,45,46,47,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,139,150,156,],[-78,30,-9,-10,67,30,67,67,67,67,67,67,67,67,67,-51,-52,-53,-54,-55,-56,67,67,67,67,67,67,67,67,]),'MAX':([7,12,13,14,36,41,43,44,45,46,47,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,139,150,156,],[-78,31,-9,-10,68,31,68,68,68,68,68,68,68,68,68,-51,-52,-53,-54,-55,-56,68,68,68,68,68,68,68,68,]),'PARENIZQ':([15,16,27,28,29,30,31,50,64,65,66,67,68,101,115,],[32,-76,43,44,45,46,47,-77,95,96,97,98,99,134,138,]),'SET':([16,17,50,],[-76,34,-77,]),'WHERE':([16,18,50,52,53,56,58,59,60,61,62,63,72,73,105,107,116,118,119,120,121,137,140,141,142,143,144,153,159,],[-76,36,-77,36,-61,-35,-38,-39,-40,-41,-42,-43,-78,-25,36,-28,-63,-62,-36,-37,-44,-26,-46,-47,-48,-49,-50,-45,-27,]),'PUNTO_Y_COMA':([16,18,35,37,48,50,52,53,55,56,58,59,60,61,62,63,70,71,72,73,83,105,107,114,116,118,119,120,121,128,129,130,131,132,133,135,137,140,141,142,143,144,145,147,149,153,155,157,158,159,160,162,164,165,169,],[-76,-78,54,-30,-23,-77,-78,-61,-29,-35,-38,-39,-40,-41,-42,-43,103,104,-78,-25,117,-78,-28,-24,-63,-62,-36,-37,-44,-67,-70,-72,-73,-74,-75,-78,-26,-46,-47,-48,-49,-50,-71,-78,-32,-45,-78,-34,-31,-27,166,168,-8,-33,-7,]),'ADD_COLUMN':([16,19,50,],[-76,38,-77,]),'DROP_COLUMN':([16,19,50,],[-76,39,-77,]),'COMA':([16,22,23,25,26,42,48,50,53,60,61,62,63,73,74,109,110,111,112,113,116,152,],[-76,41,-14,-16,-17,-15,80,-77,84,-40,-41,-42,-43,108,-13,-18,-19,-20,-21,-22,-63,161,]),'FROM':([16,20,21,22,23,25,26,42,50,74,109,110,111,112,113,],[-76,40,-11,-12,-14,-16,-17,-15,-77,-13,-18,-19,-20,-21,-22,]),'PARENDER':([16,48,49,50,58,59,60,61,62,63,75,76,77,78,79,114,123,124,125,126,127,140,141,142,143,144,146,151,152,167,],[-76,-23,81,-77,-38,-39,-40,-41,-42,-43,109,110,111,112,113,-24,140,141,142,143,144,-46,-47,-48,-49,-50,154,160,-58,-59,]),'IGUAL':([16,50,51,57,58,59,60,61,62,63,140,141,142,143,144,],[-76,-77,82,89,-38,-39,-40,-41,-42,-43,-46,-47,-48,-49,-50,]),'BETWEEN':([16,50,57,58,59,60,61,62,63,140,141,142,143,144,],[-76,-77,88,-38,-39,-40,-41,-42,-43,-46,-47,-48,-49,-50,]),'MAYOR_QUE':([16,50,57,58,59,60,61,62,63,140,141,142,143,144,],[-76,-77,90,-38,-39,-40,-41,-42,-43,-46,-47,-48,-49,-50,]),'MENOR_QUE':([16,50,57,58,59,60,61,62,63,140,141,142,143,144,],[-76,-77,91,-38,-39,-40,-41,-42,-43,-46,-47,-48,-49,-50,]),'MAYOR_IGUAL':([16,50,57,58,59,60,61,62,63,140,141,142,143,144,],[-76,-77,92,-38,-39,-40,-41,-42,-43,-46,-47,-48,-49,-50,]),'MENOR_IGUAL':([16,50,57,58,59,60,61,62,63,140,141,142,143,144,],[-76,-77,93,-38,-39,-40,-41,-42,-43,-46,-47,-48,-49,-50,]),'DIFERENTE':([16,50,57,58,59,60,61,62,63,140,141,142,143,144,],[-76,-77,94,-38,-39,-40,-41,-42,-43,-46,-47,-48,-49,-50,]),'VARCHAR':([16,50,69,],[-76,-77,101,]),'INT':([16,50,69,],[-76,-77,102,]),'JOIN':([16,50,72,73,137,],[-76,-77,106,-25,-26,]),'GROUP_BY':([16,37,50,55,56,58,59,60,61,62,63,72,73,105,107,119,120,121,135,137,140,141,142,143,144,153,159,],[-76,-30,-77,-29,-35,-38,-39,-40,-41,-42,-43,-78,-25,-78,-28,-36,-37,-44,148,-26,-46,-47,-48,-49,-50,-45,-27,]),'HAVING':([16,37,48,50,55,56,58,59,60,61,62,63,72,73,105,107,114,119,120,121,135,137,140,141,142,143,144,147,149,153,158,159,],[-76,-30,-23,-77,-29,-35,-38,-39,-40,-41,-42,-43,-78,-25,-78,-28,-24,-36,-37,-44,-78,-26,-46,-47,-48,-49,-50,156,-32,-45,-31,-27,]),'ORDER_BY':([16,37,48,50,55,56,58,59,60,61,62,63,72,73,105,107,114,119,120,121,135,137,140,141,142,143,144,147,149,153,155,157,158,159,165,],[-76,-30,-23,-77,-29,-35,-38,-39,-40,-41,-42,-43,-78,-25,-78,-28,-24,-36,-37,-44,-78,-26,-46,-47,-48,-49,-50,-78,-32,-45,163,-34,-31,-27,-33,]),'AND':([16,50,55,56,58,59,60,61,62,63,119,120,121,122,140,141,142,143,144,153,159,165,],[-76,-77,85,-35,-38,-39,-40,-41,-42,-43,-36,-37,-44,139,-46,-47,-48,-49,-50,-45,85,85,]),'OR':([16,50,55,56,58,59,60,61,62,63,119,120,121,140,141,142,143,144,153,159,165,],[-76,-77,86,-35,-38,-39,-40,-41,-42,-43,-36,-37,-44,-46,-47,-48,-49,-50,-45,86,86,]),'ON':([16,50,136,],[-76,-77,150,]),'PUNTO':([16,],[33,]),'NUM':([36,43,44,45,46,47,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,134,138,139,150,156,161,],[60,60,60,60,60,60,60,60,60,60,60,-51,-52,-53,-54,-55,-56,60,60,60,60,60,146,60,60,60,60,60,]),'STRING':([36,43,44,45,46,47,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,138,139,150,156,161,],[61,61,61,61,61,61,61,61,61,61,61,-51,-52,-53,-54,-55,-56,61,61,61,61,61,61,61,61,61,61,]),'VALUES':([81,],[115,]),'NOT_NULL':([100,102,128,129,130,131,132,133,145,154,],[130,-69,130,-70,-72,-73,-74,-75,-71,-68,]),'UNIQUE':([100,102,128,129,130,131,132,133,145,154,],[131,-69,131,-70,-72,-73,-74,-75,-71,-68,]),'PRIMARY_KEY':([100,102,128,129,130,131,132,133,145,154,],[132,-69,132,-70,-72,-73,-74,-75,-71,-68,]),'FOREIGN_KEY':([100,102,128,129,130,131,132,133,145,154,],[133,-69,133,-70,-72,-73,-74,-75,-71,-68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'select_statement':([0,],[2,]),'insert_statement':([0,],[3,]),'update_statement':([0,],[4,]),'delete_statement':([0,],[5,]),'alter_table_statement':([0,],[6,]),'opt_distinct':([7,],[12,]),'empty':([7,18,52,72,105,135,147,155,],[14,37,37,107,37,149,157,164,]),'identifier':([8,9,10,11,12,24,32,34,36,38,39,40,41,43,44,45,46,47,80,82,84,85,86,87,88,95,96,97,98,99,106,108,138,139,148,150,156,161,163,],[15,17,18,19,25,42,48,51,62,69,71,73,25,62,62,62,62,62,48,62,51,62,62,62,62,62,62,62,62,62,136,73,62,62,48,62,62,62,48,]),'select_list':([12,],[20,]),'select_items':([12,],[22,]),'select_item':([12,41,],[23,74,]),'function_call':([12,41,],[26,26,]),'opt_where_clause':([18,52,105,],[35,83,135,]),'column_list':([32,80,148,163,],[49,114,158,169,]),'assignment_list':([34,84,],[52,118,]),'assignment':([34,84,],[53,53,]),'condition':([36,85,86,150,156,],[55,119,120,159,165,]),'expression':([36,85,86,150,156,],[56,56,56,56,56,]),'operand':([36,43,44,45,46,47,85,86,87,88,95,96,97,98,99,139,150,156,],[57,75,76,77,78,79,57,57,121,122,123,124,125,126,127,153,57,57,]),'value':([36,43,44,45,46,47,82,85,86,87,88,95,96,97,98,99,138,139,150,156,161,],[58,58,58,58,58,58,116,58,58,58,58,58,58,58,58,58,152,58,58,58,152,]),'aggregate_function':([36,43,44,45,46,47,85,86,87,88,95,96,97,98,99,139,150,156,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'column_definition':([38,],[70,]),'table_list':([40,108,],[72,137,]),'comparador':([57,],[87,]),'data_type':([69,],[100,]),'opt_join_clause':([72,],[105,]),'column_constraints':([100,],[128,]),'constraint':([100,128,],[129,145,]),'opt_group_by_clause':([135,],[147,]),'value_list':([138,161,],[151,167,]),'opt_having_clause':([147,],[155,]),'opt_order_by_clause':([155,],[162,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> select_statement','statement',1,'p_statement','ParserSQL.py',13),
  ('statement -> insert_statement','statement',1,'p_statement','ParserSQL.py',14),
  ('statement -> update_statement','statement',1,'p_statement','ParserSQL.py',15),
  ('statement -> delete_statement','statement',1,'p_statement','ParserSQL.py',16),
  ('statement -> alter_table_statement','statement',1,'p_statement','ParserSQL.py',17),
  ('select_statement -> SELECT opt_distinct select_list FROM table_list opt_join_clause opt_where_clause opt_group_by_clause opt_having_clause opt_order_by_clause PUNTO_Y_COMA','select_statement',11,'p_select_statement','ParserSQL.py',21),
  ('opt_order_by_clause -> ORDER_BY column_list','opt_order_by_clause',2,'p_opt_order_by_clause','ParserSQL.py',25),
  ('opt_order_by_clause -> empty','opt_order_by_clause',1,'p_opt_order_by_clause','ParserSQL.py',26),
  ('opt_distinct -> DISTINCT','opt_distinct',1,'p_opt_distinct','ParserSQL.py',33),
  ('opt_distinct -> empty','opt_distinct',1,'p_opt_distinct','ParserSQL.py',34),
  ('select_list -> ASTERISCO','select_list',1,'p_select_list','ParserSQL.py',38),
  ('select_list -> select_items','select_list',1,'p_select_list','ParserSQL.py',39),
  ('select_items -> select_items COMA select_item','select_items',3,'p_select_items','ParserSQL.py',43),
  ('select_items -> select_item','select_items',1,'p_select_items','ParserSQL.py',44),
  ('select_item -> DISTINCT identifier','select_item',2,'p_select_item','ParserSQL.py',51),
  ('select_item -> identifier','select_item',1,'p_select_item','ParserSQL.py',52),
  ('select_item -> function_call','select_item',1,'p_select_item','ParserSQL.py',53),
  ('function_call -> COUNT PARENIZQ operand PARENDER','function_call',4,'p_function_call','ParserSQL.py',60),
  ('function_call -> SUM PARENIZQ operand PARENDER','function_call',4,'p_function_call','ParserSQL.py',61),
  ('function_call -> AVG PARENIZQ operand PARENDER','function_call',4,'p_function_call','ParserSQL.py',62),
  ('function_call -> MIN PARENIZQ operand PARENDER','function_call',4,'p_function_call','ParserSQL.py',63),
  ('function_call -> MAX PARENIZQ operand PARENDER','function_call',4,'p_function_call','ParserSQL.py',64),
  ('column_list -> identifier','column_list',1,'p_column_list','ParserSQL.py',68),
  ('column_list -> identifier COMA column_list','column_list',3,'p_column_list','ParserSQL.py',69),
  ('table_list -> identifier','table_list',1,'p_table_list','ParserSQL.py',76),
  ('table_list -> identifier COMA table_list','table_list',3,'p_table_list','ParserSQL.py',77),
  ('opt_join_clause -> JOIN identifier ON condition','opt_join_clause',4,'p_opt_join_clause','ParserSQL.py',84),
  ('opt_join_clause -> empty','opt_join_clause',1,'p_opt_join_clause','ParserSQL.py',85),
  ('opt_where_clause -> WHERE condition','opt_where_clause',2,'p_opt_where_clause','ParserSQL.py',92),
  ('opt_where_clause -> empty','opt_where_clause',1,'p_opt_where_clause','ParserSQL.py',93),
  ('opt_group_by_clause -> GROUP_BY column_list','opt_group_by_clause',2,'p_opt_group_by_clause','ParserSQL.py',100),
  ('opt_group_by_clause -> empty','opt_group_by_clause',1,'p_opt_group_by_clause','ParserSQL.py',101),
  ('opt_having_clause -> HAVING condition','opt_having_clause',2,'p_opt_having_clause','ParserSQL.py',105),
  ('opt_having_clause -> empty','opt_having_clause',1,'p_opt_having_clause','ParserSQL.py',106),
  ('condition -> expression','condition',1,'p_condition','ParserSQL.py',110),
  ('condition -> condition AND condition','condition',3,'p_condition','ParserSQL.py',111),
  ('condition -> condition OR condition','condition',3,'p_condition','ParserSQL.py',112),
  ('operand -> value','operand',1,'p_operand','ParserSQL.py',121),
  ('operand -> aggregate_function','operand',1,'p_operand','ParserSQL.py',122),
  ('value -> NUM','value',1,'p_value','ParserSQL.py',126),
  ('value -> STRING','value',1,'p_value','ParserSQL.py',127),
  ('value -> identifier','value',1,'p_value','ParserSQL.py',128),
  ('value -> ASTERISCO','value',1,'p_value','ParserSQL.py',129),
  ('expression -> operand comparador operand','expression',3,'p_expression','ParserSQL.py',133),
  ('expression -> operand BETWEEN operand AND operand','expression',5,'p_expression','ParserSQL.py',134),
  ('aggregate_function -> COUNT PARENIZQ operand PARENDER','aggregate_function',4,'p_aggregate_function','ParserSQL.py',141),
  ('aggregate_function -> SUM PARENIZQ operand PARENDER','aggregate_function',4,'p_aggregate_function','ParserSQL.py',142),
  ('aggregate_function -> AVG PARENIZQ operand PARENDER','aggregate_function',4,'p_aggregate_function','ParserSQL.py',143),
  ('aggregate_function -> MIN PARENIZQ operand PARENDER','aggregate_function',4,'p_aggregate_function','ParserSQL.py',144),
  ('aggregate_function -> MAX PARENIZQ operand PARENDER','aggregate_function',4,'p_aggregate_function','ParserSQL.py',145),
  ('comparador -> IGUAL','comparador',1,'p_comparador','ParserSQL.py',149),
  ('comparador -> MAYOR_QUE','comparador',1,'p_comparador','ParserSQL.py',150),
  ('comparador -> MENOR_QUE','comparador',1,'p_comparador','ParserSQL.py',151),
  ('comparador -> MAYOR_IGUAL','comparador',1,'p_comparador','ParserSQL.py',152),
  ('comparador -> MENOR_IGUAL','comparador',1,'p_comparador','ParserSQL.py',153),
  ('comparador -> DIFERENTE','comparador',1,'p_comparador','ParserSQL.py',154),
  ('insert_statement -> INSERT_INTO identifier PARENIZQ column_list PARENDER VALUES PARENIZQ value_list PARENDER PUNTO_Y_COMA','insert_statement',10,'p_insert_statement','ParserSQL.py',158),
  ('value_list -> value','value_list',1,'p_value_list','ParserSQL.py',162),
  ('value_list -> value COMA value_list','value_list',3,'p_value_list','ParserSQL.py',163),
  ('update_statement -> UPDATE identifier SET assignment_list opt_where_clause PUNTO_Y_COMA','update_statement',6,'p_update_statement','ParserSQL.py',170),
  ('assignment_list -> assignment','assignment_list',1,'p_assignment_list','ParserSQL.py',174),
  ('assignment_list -> assignment COMA assignment_list','assignment_list',3,'p_assignment_list','ParserSQL.py',175),
  ('assignment -> identifier IGUAL value','assignment',3,'p_assignment','ParserSQL.py',182),
  ('delete_statement -> DELETE_FROM identifier opt_where_clause PUNTO_Y_COMA','delete_statement',4,'p_delete_statement','ParserSQL.py',186),
  ('alter_table_statement -> ALTER_TABLE identifier ADD_COLUMN column_definition PUNTO_Y_COMA','alter_table_statement',5,'p_alter_table_statement','ParserSQL.py',190),
  ('alter_table_statement -> ALTER_TABLE identifier DROP_COLUMN identifier PUNTO_Y_COMA','alter_table_statement',5,'p_alter_table_statement','ParserSQL.py',191),
  ('column_definition -> identifier data_type column_constraints','column_definition',3,'p_column_definition','ParserSQL.py',198),
  ('data_type -> VARCHAR PARENIZQ NUM PARENDER','data_type',4,'p_data_type','ParserSQL.py',202),
  ('data_type -> INT','data_type',1,'p_data_type','ParserSQL.py',203),
  ('column_constraints -> constraint','column_constraints',1,'p_column_constraints','ParserSQL.py',210),
  ('column_constraints -> column_constraints constraint','column_constraints',2,'p_column_constraints','ParserSQL.py',211),
  ('constraint -> NOT_NULL','constraint',1,'p_constraint','ParserSQL.py',218),
  ('constraint -> UNIQUE','constraint',1,'p_constraint','ParserSQL.py',219),
  ('constraint -> PRIMARY_KEY','constraint',1,'p_constraint','ParserSQL.py',220),
  ('constraint -> FOREIGN_KEY','constraint',1,'p_constraint','ParserSQL.py',221),
  ('identifier -> ID','identifier',1,'p_identifier','ParserSQL.py',225),
  ('identifier -> ID PUNTO ID','identifier',3,'p_identifier','ParserSQL.py',226),
  ('empty -> <empty>','empty',0,'p_empty','ParserSQL.py',233),
]
