alter table homes add subject varchar(255);
update homes set subject = 'Home title';

CREATE TABLE user_link (
  id int(11) NOT NULL auto_increment,
  id_user int(11) NOT NULL default '0',
  title varchar(255) default NULL,
  url varchar(255) default NULL,
  intro text,
  link_picture varchar(255) default NULL,
  ordi int(11) NOT NULL default '0',
  PRIMARY KEY  (id)
);