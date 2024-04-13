from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')


@app.route('/')
def homepage():
    navbar = {
        'logo': 'img/Logo.png',
        'title': 'Filotimo',
        'items': [
            {'name': 'Home', 'link': '/'},
            {'name': 'Collection', 'link': '#collection'},
            {'name': 'Popular Genres', 'link': '#special'},
            {'name': 'Contact Us', 'link': '/contact'},
            {'name': 'About us', 'link': '#about'}
        ],
        'login': 'templates/login.html'
    }
    tracks = [
        {"id": 1, "name": "Keep Going (Buy 1 Get 1 Free)", "image": "static/img/track1.png",
         "category": "best", "description": "Backlit", "price": 19.99},
        {"id": 2, "name": "As I Lay Dying (30$ UNLIMITED)", "image": "static/img/track2.jpg",
         "category": "feat", "description": "Parallax", "price": 9.99},
        {"id": 3, "name": "Mob (Juice WRLD / Guitar Type Beat)", "image": "static/img/track3.jpg",
         "category": "new", "description": "Blanq", "price": 19.99},
        {"id": 4, "name": "Cosmic Dust | Buy 1 get 1 free", "image": "static/img/track4.jpg",
            "category": "best", "description": "Wavy Beats", "price": 25.99},
    ]

    producers = [
        {"id": 1, "name": "Nick Mira", "image": "static/img/producer1.jpg",
            "category": "feat", "location": "Richmond, Virginia"},
        {"id": 2, "name": "Metro Boomin", "image": "static/img/producer2.jpg",
            "category": "new", "location": "San Luis, United States"},
        {"id": 3, "name": "Taz Taylor", "image": "static/img/producer3.jpg",
            "category": "best", "location": "Jacksonville, Florida"},
        {"id": 4, "name": "Cxdy", "image": "static/img/producer4.jpg",
            "category": "feat", "location": "Los Angeles, California"},
    ]

    kits = [
        {"id": 1, "name": "Surface Loop Kit", "image": "static/img/track5.jpg",
            "category": "feat", "producer": "FXLICIA", "price": 45.99},
        {"id": 2, "name": "Paradise Loop Kit", "image": "static/img/track6.jpg",
            "category": "new", "producer": "BeatzDaGod", "price": 19.99},
        {"id": 3, "name": "Spaced Out", "image": "static/img/track7.jpg",
            "category": "best", "producer": "Ducko", "price": 15.99},
        {"id": 4, "name": "5k", "image": "static/img/track8.jpg",
            "category": "feat", "producer": "Fabry", "price": 35.99},
    ]
    genres = [
        {"name": "HIP HOP", "image": "static/img/hip.jpg"},
        {"name": "R&B", "image": "static/img/r&b.jpg"},
        {"name": "POP", "image": "static/img/pop.jpg"},
        {"name": "ROCK", "image": "static/img/rock.jpg"},
    ]
    offer_data = {
        "discount_text": "Discount Up To 40%",
        "offer_description": "Grand Sale Offer!",
        "button_text": "Buy Now",
        "button_link": "#"
    }
    blogs = [
        {
            "img": "img/blog.jpg",
            "title": "HEROES & VILLAINS by Metro Boomin",
            "text": "HEROES & VILLAINS debuted at #1 on the Billboard 200 during the chart week ending of December 17, 2022. It’s the third #1 album on the chart for Metro Boomin following his debut NOT ALL HEROES WEAR CAPES and collaborative project with 21 Savage, SAVAGE MODE II.",
            "author": "Genius",
            "link": "#"
        },
        {
            "img": "img/blog2.png",
            "title": "The Party Never Ends by Juice WRLD",
            "text": "This tracklist is unconfirmed. It is compiled of recent leaks, snippets, and song titles sourced from streaming services, PROs, and social media. It is purely speculative and has not been confirmed by Juice WRLD’s label. We will update this tracklist as more information comes to light.",
            "author": "Genius",
            "link": "#"
        },
        {
            "img": "img/blog3.jpg",
            "title": "Internet Money Features",
            "text": "The Internet Money collective is best known for producing hits for rappers like Drake, Juice WRLD, Young Thug, Lil Uzi Vert, and Post Malone, while also helping to break artists like Juice WRLD, Lil Tecca, and ​iann dior at the early stages of their careers.",
            "author": "Genius",
            "link": "#"
        }
    ]
    about_data = {
        "title": "About Us",
        "subtitle": "Philotimo, the origin of dreams.",
        "content": "Filotimo, we are a group of producers who want to improve this world, make it something different, we want that for all the producers of the world, they can fulfill their dream in a more accessible way, that for all is something ideal. We are a group that does not have access to a lot of money, we are just starting and we want that those who can not have that support and money to sell their music, can make it real.",
        "img_src": "static/img/filotimo.jpeg"
    }
    popular_data = {
        "title": "Popular Of This Year",
        "top_rated": [
            {"name": "As I Lay Dying (30$ UNLIMITED)", "price": "$ 9.99",
             "producer": "Parallax", "img_src": "static/img/track2.jpg"},
            {"name": "Mob (Juice WRLD / Guitar Type Beat)", "price": "$ 19.99",
             "producer": "Blanq", "img_src": "static/img/track3.jpg"},
            {"name": "Paradise Loop Kit", "price": "$ 19.99",
                "producer": "BeatzDaGod", "img_src": "static/img/track6.jpg"}
        ],
        "best_selling": [
            {"name": "Spaced Out", "price": "$ 15.99",
                "producer": "Ducko", "img_src": "static/img/track7.jpg"},
            {"name": "Cosmic Dust | Buy 1 Get 1 Free", "price": "$ 25.99",
                "producer": "Wavy Beats", "img_src": "static/img/track4.jpg"},
            {"name": "5k", "price": "$ 35.99", "producer": "Fabry",
                "img_src": "static/img/track8.jpg"}
        ],
        "top_rated_producers": [
            {"name": "Nick Mira", "location": "Richmond, Virginia",
                "img_src": "static/img/producer1.jpg"},
            {"name": "Metro Boomin", "location": "San Luis, United States",
                "img_src": "static/img/producer2.jpg"},
            {"name": "Taz Taylor", "location": "Jacksonville, Florida",
                "img_src": "static/img/producer3.jpg"}
        ]
    }
    newsletter_data = {
        "title": "Newsletter Subscription",
        "description": "If you want to know more about our news, opportunities, challenges and more... subscribe only with your email address."
    }
    footer_data = {
        "brand": {
            "name": "Attire",
            "url": "index.html"
        },
        "description": "Welcome to our music community where creators come together to share and explore the world of music. At Splice, we believe in the power of collaboration and creativity.",
        "links": [
            {"text": "Home", "url": "#"},
            {"text": "Collection", "url": "#"},
            {"text": "Blogs", "url": "#"},
            {"text": "About Us", "url": "#"}
        ],
        "contact": {
            "address": "Ciudad Bolivar, Bogota, Colombia",
            "email": "contact@filotimo.com",
            "phone": "+57 (321) 385-0404"
        },
        "social_media": [
            {"name": "Facebook", "url": "https://www.facebook.com/",
             "icon": "fab fa-facebook-f"},
            {"name": "Twitter", "url": "https://twitter.com/",
                "icon": "fab fa-twitter"},
            {"name": "Instagram", "url": "https://www.instagram.com/",
             "icon": "fab fa-instagram"}
        ]
    }

    audio_url = "static/audio/aa.mp3"
    return render_template('index.html', navbar=navbar, tracks=tracks, producers=producers, kits=kits, genres=genres, offer_data=offer_data, blogs=blogs, about_data=about_data, popular_data=popular_data, newsletter_data=newsletter_data, footer_data=footer_data, audio_url=audio_url)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Login exitoso'
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return 'Registro exitoso'
    return render_template('register.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
