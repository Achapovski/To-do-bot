from dataclasses import dataclass
from aiogram import Bot
from environs import Env


@dataclass
class BotConfig:
    bot_token: str


@dataclass
class Config:
    bot: BotConfig


def load_config_settings(path: str | None = None):
    env = Env()
    env.read_env(path)
    return Config(
        bot=BotConfig(
            bot_token=env("BOT_TOKEN")
        ),
    )

