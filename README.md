# PyPi-connect_mongodb

Connect python with MongoDB


### Installation
Run below commandto install whole package

```pip install connect_mongodb```


### Prerequisite
pymongo must be installed
To install pymongo, run below command

```pip install pymongo```


### Import
```from connect_mongodb import Mongodb```


### Connect to Mongodb
```con=Mongodb()``` 
```con.connection(connection_url, database_name=None)```  
        connection function establishes a connection with mongo server 

        Parameters:

        ->connection_url: connection url with password
        database_name(optional): name of the database
        
    
### Create Database
```con.create_database(database_name)```   
        create_database function helps to create a new database 

        Parameters:

        ->database_name: name of the database
        
        
### Check existing Database
```con.available_database()```    
        available_database function returns list of all the existing database 
        

### Create Collection
```con.create_collection(collection_name)```    
        Function create_collection is used to create a new collection    
         
        Parameters:   

        ->collection_name: name of the collection
     

### Record Insertion
```con.insert(collection_name, record)```  
        Insert function is used to insert value in the table  

        Parameters:  

        ->collection_name: name of the collection
        ->record: data to be inserted
            -to insert one record datatype should be dictionary
            -to insert many record datatype should be list
        

### Finding Records
```con.find(collection_name)```   
        find function is used find all the records in a collection  

        Parameters:  

        ->collection_name: name of the collection
        
        
### Updating a Record 
```con.update(self, collection_name, present_record, new_record))```   
        update function is used to alter/update the record  

        Parameters:  

        ->collection_name: collection name
        ->present_record: existing record
            -datatype as dict
        ->new_record: new record
            -datatype as dict
        
    
### Delete
```con.delete(collection_name,query)```  
        delete function is used to delete record from collection  

        Parameters:  

        ->collection_name: name of the collection
        ->query: any condition in that particular record
            -datatype as dictionary
        

### Drop a Connection
```con.drop_collection(self, collection_name)```    
        drop_collection function is used to drop the collection  

        Parameters:  

        ->collection_name: name of the collection
        
        
