from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    """Animal model representing animals in the zoo"""
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    # Relationships
    zookeeper = db.relationship('Zookeeper', back_populates='animals')
    enclosure = db.relationship('Enclosure', back_populates='animals')

    def __repr__(self):
        return f'<Animal {self.name}, {self.species}>'

class Zookeeper(db.Model):
    """Zookeeper model representing zoo staff"""
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.String)

    # Relationships
    animals = db.relationship('Animal', back_populates='zookeeper')

    def __repr__(self):
        return f'<Zookeeper {self.name}>'

class Enclosure(db.Model):
    """Enclosure model representing animal habitats"""
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String, nullable=False)  # grass, sand, or water
    open_to_visitors = db.Column(db.Boolean, default=False)

    # Relationships
    animals = db.relationship('Animal', back_populates='enclosure')

    def __repr__(self):
        return f'<Enclosure {self.environment}>'