# resources.py

def get_video_link(career):
    """
    Returns a relevant YouTube link for the given career.
    """
    videos = {
        "Data Scientist": "https://www.youtube.com/watch?v=ua-CiDNNj30",
        "Artist": "https://www.youtube.com/watch?v=sn8rG2f-5-w",
        "Teacher": "https://www.youtube.com/watch?v=U1xA2WkDzDQ",
        "Doctor": "https://www.youtube.com/watch?v=9cR2bCcyRyo",
        "Engineer": "https://www.youtube.com/watch?v=Y1nZ0Ogsr0E",
        "Lawyer": "https://www.youtube.com/watch?v=yV94gBq0K7E",
        "Entrepreneur": "https://www.youtube.com/watch?v=bJzE7ySCi9I",
        "Psychologist": "https://www.youtube.com/watch?v=4UeYGS0UUq4",
        "Software Developer": "https://www.youtube.com/watch?v=NGD53w5w5jM",
        "Nurse": "https://www.youtube.com/watch?v=b1gIdmfzVss",
        "Mechanical Engineer": "https://www.youtube.com/watch?v=Jzxe81vWvRs",
        "Civil Engineer": "https://www.youtube.com/watch?v=qTkzM9fAYwk",
        "Scientist": "https://www.youtube.com/watch?v=rkZl2gsLUp4",
        "Marketing Manager": "https://www.youtube.com/watch?v=bhJgRUZgjH0",
        "Financial Analyst": "https://www.youtube.com/watch?v=wvT4w-RtCM4"
    }
    return videos.get(career, "https://www.youtube.com")


def get_quote():
    """
    Returns a random motivational quote.
    """
    import random
    quotes = [
        "Believe in yourself and all that you are. 💪",
        "Your career is your journey — make it count! ✨",
        "Success is not in what you have, but who you are. 🌟",
        "Keep going. Everything you need will come to you. 🚀",
        "Dream big. Work hard. Stay focused. 🙌",
        "Opportunities don’t happen, you create them. 🔑"
    ]
    return random.choice(quotes)
