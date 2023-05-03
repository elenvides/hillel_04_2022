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
    def __init__(self, user: User):
        self.user = user

    @abstractmethod
    def post_a_message(self, post: SocialPost) -> None:
        pass

    @abstractmethod
    def _authorize(self) -> None:
        pass

    @abstractmethod
    def _sign_out(self) -> None:
        pass

    def __enter__(self):
        self._authorize()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._sign_out()


class YoutubeChannel(SocialChannel):
    def post_a_message(self, post: SocialPost) -> None:
        print("Posted to Youtube:", post)

    def _authorize(self) -> None:
        print(f"Authorized user {self.user.username} on Youtube")

    def _sign_out(self) -> None:
        print(f"Signed out user {self.user.username} from Youtube")


class FacebookChannel(SocialChannel):
    def post_a_message(self, post: SocialPost) -> None:
        print("Posted to Facebook:", post)

    def _authorize(self) -> None:
        print(f"Authorized user {self.user.username} on Facebook")

    def _sign_out(self) -> None:
        print(f"Signed out user {self.user.username} from Facebook")


class TwitterChannel(SocialChannel):
    def post_a_message(self, post: SocialPost) -> None:
        print("Posted to Twitter:", post)

    def _authorize(self) -> None:
        print(f"Authorized user {self.user.username} on Twitter")

    def _sign_out(self) -> None:
        print(f"Signed out user {self.user.username} from Twitter")


def process_scheduled_messages(
    posts: List[SocialPost], channels: List[SocialChannel]
) -> None:
    while posts:
        current_time = time()
        for post in posts:
            if post.timestamp <= current_time:
                for channel in channels:
                    with channel as authorized_channel:
                        authorized_channel.post_a_message(post)
                posts.remove(post)
        sleep(1)


def main():
    user = User("Jane", "strong_password")

    channels = [
        YoutubeChannel(user),
        FacebookChannel(user),
        TwitterChannel(user),
    ]

    posts = [
        SocialPost("First post", 5),
        SocialPost("Second post", 2),
    ]

    process_scheduled_messages(posts, channels)


if __name__ == "__main__":
    main()
