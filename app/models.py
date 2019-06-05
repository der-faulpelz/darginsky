# coding: utf-8
from sqlalchemy import Column, ForeignKey, String, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Cognate(Base):
    __tablename__ = 'cognates'

    id = Column(INTEGER(11), primary_key=True)
    no = Column(String(10), unique=True)


class Dialect(Base):
    __tablename__ = 'dialects'

    id = Column(INTEGER(11), primary_key=True)
    dialect = Column(String(20), unique=True)


class Frame(Base):
    __tablename__ = 'frames'

    id = Column(INTEGER(11), primary_key=True)
    frame = Column(String(10))


class Hyperlexeme(Base):
    __tablename__ = 'hyperlexemes'

    id = Column(INTEGER(11), primary_key=True)
    hyperlexeme = Column(String(30), unique=True)


class NounClass(Base):
    __tablename__ = 'noun_classes'

    id = Column(INTEGER(11), primary_key=True, server_default=text("'0'"))
    _class = Column('class', String(5), unique=True)


class PartOfSpeech(Base):
    __tablename__ = 'part_of_speech'

    id = Column(INTEGER(11), primary_key=True)
    pos = Column(LONGTEXT)


class TranslationRu(Base):
    __tablename__ = 'translation_rus'

    id = Column(INTEGER(11), primary_key=True)
    translation = Column(String(100), unique=True)


class Grammem(Base):
    __tablename__ = 'grammems'

    id = Column(INTEGER(11), primary_key=True)
    grammem = Column(String(20), unique=True)
    pos_id = Column(ForeignKey('part_of_speech.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)

    pos = relationship('PartOfSpeech')


class Word(Base):
    __tablename__ = 'words'

    id = Column(INTEGER(11), primary_key=True)
    word = Column(LONGTEXT)
    pos_id = Column(ForeignKey('part_of_speech.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    dialect_id = Column(ForeignKey('dialects.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    hyperlexeme_id = Column(ForeignKey('hyperlexemes.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    translation_rus_id = Column(ForeignKey('translation_rus.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    comment = Column(LONGTEXT)

    dialect = relationship('Dialect')
    hyperlexeme = relationship('Hyperlexeme')
    pos = relationship('PartOfSpeech')
    translation_rus = relationship('TranslationRu')


class Form(Base):
    __tablename__ = 'forms'

    id = Column(INTEGER(11), primary_key=True)
    form = Column(LONGTEXT)
    word_id = Column(ForeignKey('words.id', ondelete='CASCADE'), index=True)
    gram_id = Column(ForeignKey('grammems.id', onupdate='CASCADE'), index=True)
    comment = Column(LONGTEXT)

    gram = relationship('Grammem')
    word = relationship('Word')


class HasClas(Base):
    __tablename__ = 'has_class'

    id = Column(INTEGER(11), primary_key=True)
    word_id = Column(ForeignKey('words.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    class_id = Column(ForeignKey('noun_classes.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)

    _class = relationship('NounClass')
    word = relationship('Word')


class HasCognate(Base):
    __tablename__ = 'has_cognate'

    id = Column(INTEGER(11), primary_key=True)
    word_id = Column(ForeignKey('words.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    cognate_id = Column(ForeignKey('cognates.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)

    cognate = relationship('Cognate')
    word = relationship('Word')


class HasVerbFrame(Base):
    __tablename__ = 'has_verb_frame'

    id = Column(INTEGER(11), primary_key=True)
    word_id = Column(ForeignKey('words.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    frame_id = Column(ForeignKey('frames.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)

    frame = relationship('Frame')
    word = relationship('Word')


class VerbRoot(Base):
    __tablename__ = 'verb_roots'

    id = Column(INTEGER(11), primary_key=True)
    root = Column(String(25), unique=True)
    gram_id = Column(ForeignKey('grammems.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)

    gram = relationship('Grammem')


class HasVerbRoot(Base):
    __tablename__ = 'has_verb_root'

    id = Column(INTEGER(11), primary_key=True)
    word_id = Column(ForeignKey('words.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)
    verb_root_id = Column(ForeignKey('verb_roots.id', ondelete='SET NULL', onupdate='CASCADE'), index=True)

    verb_root = relationship('VerbRoot')
    word = relationship('Word')






