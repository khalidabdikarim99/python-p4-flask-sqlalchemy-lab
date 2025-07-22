from app import app, db
from models import Animal, Zookeeper, Enclosure

def clear_data():
    """Clear all existing data from the tables"""
    db.session.query(Animal).delete()
    db.session.query(Zookeeper).delete()
    db.session.query(Enclosure).delete()
    db.session.commit()

def seed_zookeepers():
    """Create and return a list of zookeepers"""
    zookeepers = [
        Zookeeper(name="Dylan Taylor", birthday="1990-05-15"),
        Zookeeper(name="Stephanie Contreras", birthday="1996-09-20"),
        Zookeeper(name="Marcus Wright", birthday="1985-11-03"),
        Zookeeper(name="Olivia Chen", birthday="1992-07-28"),
        Zookeeper(name="Raj Patel", birthday="1988-03-12")
    ]
    db.session.add_all(zookeepers)
    db.session.commit()
    return zookeepers

def seed_enclosures():
    """Create and return a list of enclosures"""
    enclosures = [
        Enclosure(environment="grass", open_to_visitors=True),
        Enclosure(environment="sand", open_to_visitors=False),
        Enclosure(environment="water", open_to_visitors=True),
        Enclosure(environment="grass", open_to_visitors=True),
        Enclosure(environment="sand", open_to_visitors=True)
    ]
    db.session.add_all(enclosures)
    db.session.commit()
    return enclosures

def seed_animals(zookeepers, enclosures):
    """Create animals with relationships to zookeepers and enclosures"""
    animals = [
        Animal(name="Logan", species="Snake", 
               zookeeper=zookeepers[0], enclosure=enclosures[0]),
        Animal(name="Leo", species="Lion", 
               zookeeper=zookeepers[1], enclosure=enclosures[1]),
        Animal(name="Misty", species="Dolphin", 
               zookeeper=zookeepers[2], enclosure=enclosures[2]),
        Animal(name="Bella", species="Elephant", 
               zookeeper=zookeepers[3], enclosure=enclosures[3]),
        Animal(name="Rocky", species="Tiger", 
               zookeeper=zookeepers[4], enclosure=enclosures[4]),
        Animal(name="Zoe", species="Zebra", 
               zookeeper=zookeepers[0], enclosure=enclosures[1]),
        Animal(name="Oscar", species="Otter", 
               zookeeper=zookeepers[1], enclosure=enclosures[2]),
        Animal(name="Gina", species="Giraffe", 
               zookeeper=zookeepers[2], enclosure=enclosures[3]),
        Animal(name="Pablo", species="Penguin", 
               zookeeper=zookeepers[3], enclosure=enclosures[4]),
        Animal(name="Sammy", species="Shark", 
               zookeeper=zookeepers[4], enclosure=enclosures[0])
    ]
    db.session.add_all(animals)
    db.session.commit()
    return animals

if __name__ == '__main__':
    with app.app_context():
        print("Clearing old data...")
        clear_data()
        
        print("Seeding zookeepers...")
        zookeepers = seed_zookeepers()
        
        print("Seeding enclosures...")
        enclosures = seed_enclosures()
        
        print("Seeding animals...")
        animals = seed_animals(zookeepers, enclosures)
        
        print("Database seeded successfully!")
        print(f"Created: {len(zookeepers)} zookeepers, {len(enclosures)} enclosures, {len(animals)} animals")