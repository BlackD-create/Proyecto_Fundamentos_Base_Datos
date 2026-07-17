create database gestion_universidad;
use gestion_universidad;
create table estudiante(
	matricula varchar(15) primary key,
    nombre varchar(50) not null,
    correo varchar(50) unique not null
);
create table departamento(
	codigo int primary key,
    nombre varchar(50) not null
);
create table docente(
    cedula varchar(10) primary key,
    nombre varchar(100) not null,
    especialidad varchar(100) not null,
    codigo_dep int not null,
    foreign key(codigo_dep) references departamento(codigo) on update cascade on delete restrict
);
create table curso(
    codigo int primary key,
    nombre varchar(100) not null,
    creditos int not null check(creditos>0),
    cedula varchar(10) not null,
    codigo_dep int not null,
    foreign key(cedula) references docente(cedula) on update cascade on delete restrict,
    foreign key(codigo_dep) references departamento(codigo) on update cascade on delete restrict
);
create table inscripcion(
    id int auto_increment primary key,
    matricula varchar(15) not null,
    codigo_curso int not null,
    periodo varchar(20) not null,
    foreign key(matricula) references estudiante(matricula) on update cascade on delete cascade,
    FOREIGN KEY(codigo_curso) REFERENCES curso(codigo) on update cascade on delete restrict,
    unique(matricula,codigo_curso,periodo)
);
create table evaluacion(
    id_eval int auto_increment primary key,
    tipo varchar(50) not null,
    nota decimal(5,2) not null check(nota>=0 and nota<=10),
    id int not null,
    foreign key (id) references inscripcion(id) on update cascade on delete cascade
);