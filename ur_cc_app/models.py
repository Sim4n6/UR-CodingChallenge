from haversine import haversine

from ur_cc_app import db, ma


class Shop(db.Model):

    __tablename__ = "shops"

    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    coord_type = db.Column(db.String(50), nullable=False)
    coordinate_lat = db.Column(db.Float, nullable=False)
    coordinate_long = db.Column(db.Float, nullable=False)

    def haversine(self, coord_user_lat, coord_user_lng):
        # haversine compute the distsance btw user location and shop location
        return haversine(
            (self.coordinate_lat, self.coordinate_long),
            (coord_user_lat, coord_user_lng),
        )

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


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(150))

    def __repr__(self):
        return f"<User {self.name}>"


class UsersSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "password")


user_schema = UsersSchema(many=True)


class User_Shop(db.Model):
    __tablename__ = "users_shops"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    shop_id = db.Column(db.Integer, db.ForeignKey("shops.id"))
    user = db.relationship("User", backref=db.backref("shops"))
    shop = db.relationship("Shop", backref=db.backref("users"))

    def __repr__(self):
        return f"<User_id {self.user_id} <--> Shop_id {self.shop_id}>"


class User_Shop_Schema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "shop_id")


user_shop_schema = User_Shop_Schema(many=True)
