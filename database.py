import sqlite3

conn = sqlite3.connect('database.db')
sql_create_image_denoise_data_table = 'CREATE TABLE IF NOT EXISTS image_denoise_data (id integer PRIMARY KEY, mse real not null, peak_signal real not null,' \
                                'wavelet_fk text NOT NULL, image_type_fk text NOT NULL, FOREIGN KEY (wavelet_fk) REFERENCES wavelet_family (wavelet), ' \
                                'FOREIGN KEY (image_type_fk) REFERENCES image_color_map (image_type));'

sql_create_wavelet_family_table = 'CREATE TABLE IF NOT EXISTS wavelet_family (wavelet text PRIMARY KEY);'

sql_create_image_color_map_table = "CREATE TABLE IF NOT EXISTS image_color_map (image_type text PRIMARY KEY);"


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)
wavelet_family_label_list = ['db1',
                                 'db2',
                                 'db3',
                                 'dmey',
                                 'gaus1',
                                 'gaus2',
                                 'haar',
                                 'sym2',
                                 'sym3',
                                 'bior1.3',
                                 'bior2.2'
                                 ]
c = conn.cursor()
#for item in wavelet_family_label_list:
#c.execute("insert into image_color_map (image_type) values ('grayscale')")
#conn.execute("INSERT INTO image_denoise_data (id, mse, wavelet_fk, peak_signal, image_type_fk) VALUES (1, 17.322, 'db1', 12.287, 'RGB')")

#create_table(conn, sql_create_image_denoise_data_table)
#conn.execute("INSERT INTO image_denoise_data (id, mse, wavelet_fk, peak_signal, image_type_fk) VALUES (1, 17.322, 'db1', 12.287, 'RGB')")
conn.commit()

