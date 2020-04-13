create table Shoes
(
    id   int      not null
        primary key,
    name varchar(128) not null
) character set = utf8mb4;

create table ShoesColor
(
    color_id   int  not null
        primary key,
    color_name varchar(128) null,
    img_link   varchar(512) null
) character set = utf8mb4;

create table ShoesPrice
(
    shoes_id       int  not null,
    shoes_color_id int  not null,
    size           int  not null,
    update_time    date not null,
    price          int  not null,
    primary key (shoes_id, shoes_color_id, size, update_time),
    constraint ShoesPrice_ShoesColor_color_id_fk
        foreign key (shoes_color_id) references ShoesColor (color_id)
            on update cascade on delete cascade,
    constraint ShoesPrice_Shoes_id_fk
        foreign key (shoes_id) references Shoes (id)
            on update cascade on delete cascade
)character set = utf8mb4;


