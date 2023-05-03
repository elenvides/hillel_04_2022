from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from time import sleep, time
from typing import List


@dataclass
class User:
    username: str
    password: str


@dataclass
class SocialPost:
    message: str
    delay: int
    timestamp: int = field(init=False)

    def __post_init__(self):
        self.timestamp = int(time() + self.delay)


class SocialChannel(ABC):
    def __init__(self, subscribers_count: int):
        self.subscribers_count = subscribers_count

    @abstractmethod
    def post_a_message(self, post: SocialPost) -> None:
        pass

    @abstractmethod
    def authorize(self, user: User) -> None:
        pass

    @abstractmethod
    def sign_out(self) -> None:
        pass


class YoutubeChannel(SocialChannel):
    def __init__(self, subscribers_count: int = 50):
        super().__init__(subscribers_count)

    def post_a_message(self, post: SocialPost) -> None:
        print("Posted to Youtube:", post)

    def authorize(self, user) -> None:
        print(f"Authorized user {user.username} on Youtube")

    def sign_out(self) -> None:
        print("Signed out from Youtube")


class FacebookChannel(SocialChannel):
    def __init__(self, subscribers_count: int = 70):
        super().__init__(subscribers_count)

    def post_a_message(self, post: SocialPost) -> None:
        print("Posted to Facebook:", post)

    def authorize(self, user) -> None:
        print(f"Authorized user {user.username} on Facebook")

    def sign_out(self) -> None:
        print("Signed out from Facebook")


class TwitterChannel(SocialChannel):
    def __init__(self, subscribers_count: int = 40):
        super().__init__(subscribers_count)

    def post_a_message(self, post: SocialPost) -> None:
        print("Posted to Twitter:", post)

    def authorize(self, user) -> None:
        print(f"Authorized user {user.username} on Twitter")

    def sign_out(self) -> None:
        print("Signed out from Twitter")


class SocialChannelProcessor:
    def __init__(self, social_chanel: SocialChannel):
        self._social_chanel = social_chanel

    def post_a_message(self, user: User, post: SocialPost):
        self._social_chanel.authorize(user)
        self._social_chanel.post_a_message(post)


def process_scheduled_messages(
    posts: List[SocialPost], channels: List[SocialChannel], user: User
) -> None:
    while posts:
        current_time = time()
        for post in posts:
            if post.timestamp <= current_time:
                for channel in channels:
                    channel_processor = SocialChannelProcessor(channel)
                    channel_processor.post_a_message(user, post)
                posts.remove(post)
        sleep(1)


def main():
    user = User("Jane", "strong_password")

    channels = [
        YoutubeChannel(),
        FacebookChannel(),
        TwitterChannel(),
    ]

    posts = [
        SocialPost("First post", 5),
        SocialPost("Second post", 2),
    ]

    process_scheduled_messages(posts, channels, user)


if __name__ == "__main__":
    main()
