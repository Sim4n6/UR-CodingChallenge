from ur_cc_app import db
from ur_cc_app import ma


class Shops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    coord_type = db.Column(db.String(50), nullable=False)
    coordinate_lat = db.Column(db.Float, nullable=False)
    coordinate_long = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Shop {self.name}>"


class ShopsSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "picture",
            "name",
            "email",
            "city",
            "coord_type",
            "coordinate_lat",
            "coordinate_long",
        )


shop_schema = ShopsSchema(many=True)
