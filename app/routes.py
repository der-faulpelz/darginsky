from app import app
from flask import render_template, request, jsonify
from app.forms import SearchForm, LoginForm
from app.models import Word, Grammem, Form, PartOfSpeech, TranslationRu, Frame, HasVerbFrame
from app.config.database import session
from sqlalchemy import or_
from app.scripts import transcr


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    form = SearchForm()

    if request.method == "POST":
        dialect = form.dialect.data
        #if form.validate_on_submit():
        if dialect == "0":

            s_word = session.query(Word).join(TranslationRu, TranslationRu.id == Word.translation_rus_id). \
                join(Form, Form.word_id == Word.id). \
                filter(or_(Word.word == form.searched_word.data,
                           TranslationRu.translation.like('% {}%'.format(form.searched_word.data)),
                           TranslationRu.translation.like(form.searched_word.data + "%"))).all()

        else:
            s_word = session.query(Word).join(TranslationRu, TranslationRu.id == Word.translation_rus_id). \
                filter(or_(Word.word == form.searched_word.data,
                           TranslationRu.translation.like('% {}%'.format(form.searched_word.data)),
                           TranslationRu.translation.like(form.searched_word.data + "%"))). \
                filter(Word.dialect_id.in_(dialect)).all()


        num_s_words = len(s_word)
        wordforms = []
        synonims = []

        for i in s_word:
            a = session.query(Word and Form).join(Word, Word.id == Form.word_id).filter(Word.id == i.id).all()

            wordforms.append((i.id, a))

            b = session.query(Word).filter(Word.hyperlexeme_id == i.hyperlexeme_id).filter(Word.id != i.id).all()
            synonims += b

        if s_word:
            print (s_word)
            return render_template('word.html', words=s_word, wordforms=dict(wordforms), synonims=synonims,
                                   form=form, num=num_s_words, transcr=transcr)

        """
        elif similar_words:
            return render_template('like.html', similar_words=similar_words, database_words=database_words, form=form,
                                   transcr=transcr)

        elif similar_words == []:  # empty set
            return render_template('error.html', form=form)"""

    return render_template("index.html", form=form)


@app.route('/prosearch', methods=["GET", "POST"])
def prosearch():
    form = SearchForm()
    query_parameters = []
    query_result = []
    #form.grammeme.choices = [("1", "Выберите часть речи, чтобы выбрать формы")]
    #form.grammeme.choices = [(grammeme.id, grammeme.grammem) for grammeme in session.query(Grammem).filter(Grammem.pos_id == "1").all()]

    if request.method == "POST":

        # Поиск синонимов
        prochoice = form.prochoice.data
        dialect_choice = request.form.getlist("prodialect")
        pos = form.pos.data
        nounclass = request.form.getlist("nounclass")
        verbframe = request.form.getlist("verbframe")
        grammeme = request.form.getlist("grammeme")
        # for i in (prochoice, dialect_choice, pos, nounclass, verbframe, grammeme):
        #    query_parameters.append(i)
        # print (query_parameters)
        # grammeme = session.query(Grammem).filter_by(id=form.grammeme.data).first()
        # form.grammeme.choices = [(grammeme.id, grammeme.grammem) for grammeme in
        #                        session.query(Grammem).filter(Grammem.pos_id.in_(pos)).all()]

        ######################################################
        ## Поиск по форме или переводу

        if pos in ["0", "3", "4", "5"]:
            s_word = session.query(Word).join(TranslationRu, TranslationRu.id == Word.translation_rus_id). \
                join(Form, Form.word_id == Word.id). \
                filter(or_(Word.word == form.searched_word.data,
                           TranslationRu.translation.like('% {}%'.format(form.searched_word.data)), TranslationRu.translation.like(form.searched_word.data + "%"))). \
                filter(Word.dialect_id.in_(dialect_choice)).all()


        elif pos == "1":

            s_word = session.query(Word).join(TranslationRu, TranslationRu.id == Word.translation_rus_id). \
                join(Form, Form.word_id == Word.id). \
                join(Frame and HasVerbFrame, Word.id == HasVerbFrame.word_id and Frame.id == HasVerbFrame.frame_id). \
                filter(or_(Word.word == form.searched_word.data,
                           TranslationRu.translation.like('% {}%'.format(form.searched_word.data)),
                           TranslationRu.translation.like(form.searched_word.data + "%"))). \
                filter(Word.dialect_id.in_(dialect_choice)). \
                filter(Word.pos_id.in_(pos)). \
                filter(Form.gram_id.in_(grammeme)). \
                filter(HasVerbFrame.frame_id.in_(verbframe)).all()

        elif pos == "2":

            s_word = session.query(Word).join(TranslationRu, TranslationRu.id == Word.translation_rus_id). \
                join(Form, Form.word_id == Word.id). \
                filter(or_(Word.word == form.searched_word.data,
                           TranslationRu.translation.like('% {}%'.format(form.searched_word.data)),
                           TranslationRu.translation.like(form.searched_word.data + "%"))). \
                filter(Word.dialect_id.in_(dialect_choice)). \
                filter(Word.pos_id.in_(pos)). \
                filter(Form.gram_id.in_(grammeme)).all()


        ids = []
        for element in s_word:
            ids.append(element.id)

        word_forms = session.query(Form).join(Word, Word.id == Form.word_id).filter(Word.id.in_(ids)).all()

        synonims = []
        for i in s_word:
            b = session.query(Word).filter(Word.hyperlexeme_id == i.hyperlexeme_id).filter(Word.id != i.id).all()
            synonims += b

        sameroot = []
        for i in s_word:
            x = session.query(Word).join(Frame and HasVerbFrame, Word.id == HasVerbFrame.word_id and Frame.id == HasVerbFrame.frame_id).\
                filter(Word.id == i.id).all()
            sameroot.append(x)

        if prochoice in ["3", '4']:
            print ([i for i in sameroot])

        if prochoice == "2" and synonims:
            return render_template("like.html", form=form, similar_words=synonims)

        elif prochoice == "1":

            if len(s_word) == 1:
                return render_template("word.html", form=form, words=set(s_word), forms=set(word_forms), similar_words=synonims)

            elif len(s_word) > 1:
                return render_template("like.html", form=form, similar_words=set(s_word), forms=set(word_forms))

            else:
                return render_template("error.html", form=form)

    return render_template("prosearch.html", form=form)


@app.route('/prosearch/grammeme/<pos>')
def grammeme(pos):
    #pos = session.query(PartOfSpeech).filter(PartOfSpeech.pos == pos).first()
    grammemes = session.query(Grammem).join(PartOfSpeech).filter(Grammem.pos_id == "{}".format(pos)).all()
    grammemeArray = []

    for grammeme in grammemes:
        grammemeObj = {}
        grammemeObj['id'] = grammeme.id
        grammemeObj['grammem'] = grammeme.grammem
        grammemeArray.append(grammemeObj)

    return jsonify({'grammemes' : grammemeArray})


@app.route('/word')
@app.route("/word/<input>", methods=['GET', "POST"])
def word(input):
    form = SearchForm()
    s_word = session.query(Word).filter(Word.word == input).all()
    wordforms = []
    synonims = []

    for i in s_word:
        a = session.query(Word and Form).join(Word, Word.id == Form.word_id).filter(Word.id == i.id).all()

        wordforms.append((i.id, a))

        b = session.query(Word).filter(Word.hyperlexeme_id == i.hyperlexeme_id).filter(Word.id != i.id).all()
        synonims += b

    #прописать путь к аудио и дополнительную информацию

    return render_template('word.html',form=form, words=s_word, wordforms=dict(wordforms), synonims=synonims)


@app.route('/login', methods=['GET', "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "It works"
    return render_template('jisho.html', title='Sign In', form=form)


@app.route('/database')
def database():

    database_words = session.query(Word and Form).join(Word, Word.id == Form.word_id).order_by(Word.id)
    #database_words = session.query(Form).order_by(Form.id)

    return render_template("database.html", title="Database", database_words=database_words)


@app.route("/about")
def about():
    return render_template("about.html", title="About")



""""  elif dialect == "3":  # ищем только в Тантах

            if cyrillic.match(form.searched_word.data):

                s_word = session.query(Word).filter(Word.dialect_id == 1,
                                                    Word.word == transcr_drg(form.searched_word.data)).all()
            else:
                s_word = session.query(Word).filter(Word.dialect_id == 1, Word.word == (form.searched_word.data)).all()
            t_word = session.query(Word).filter(Word.dialect_id == 1,
                                                Word.translation_rus == (form.searched_word.data)).all()
            similar_words = session.query(Word).filter(Word.dialect_id == 1,
                                                       Word.word.like(
                                                           '%{}%'.format(form.searched_word.data[0:3]))).all()

            ######################################################
        elif dialect == "4":  # ищем только в Калкни

            if cyrillic.match(form.searched_word.data):

                s_word = session.query(Word).filter(Word.dialect_id == 2,
                                                    Word.word == transcr_drg(form.searched_word.data)).all()
            else:
                s_word = session.query(Word).filter(Word.dialect_id == 2, Word.word == (form.searched_word.data)).all()
            t_word = session.query(Word).filter(Word.dialect_id == 2,
                                                Word.translation_rus == (form.searched_word.data)).all()
            similar_words = session.query(Word).filter(Word.dialect_id == 2,
                                                       Word.word.like(
                                                           '%{}%'.format(form.searched_word.data[0:3]))).all()

            ######################################################"""