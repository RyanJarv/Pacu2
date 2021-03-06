# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2021-12-31T02:54:04+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Annotated, Any, List, Optional

from pydantic import BaseModel, Field, SecretStr


class DeleteLexiconOutput(BaseModel):
    pass


class LexiconNotFoundException(BaseModel):
    __root__: Any


class ServiceFailureException(LexiconNotFoundException):
    pass


class InvalidNextTokenException(LexiconNotFoundException):
    pass


class InvalidTaskIdException(LexiconNotFoundException):
    pass


class SynthesisTaskNotFoundException(LexiconNotFoundException):
    pass


class PutLexiconOutput(DeleteLexiconOutput):
    pass


class InvalidLexiconException(LexiconNotFoundException):
    pass


class UnsupportedPlsAlphabetException(LexiconNotFoundException):
    pass


class UnsupportedPlsLanguageException(LexiconNotFoundException):
    pass


class LexiconSizeExceededException(LexiconNotFoundException):
    pass


class MaxLexemeLengthExceededException(LexiconNotFoundException):
    pass


class MaxLexiconsNumberExceededException(LexiconNotFoundException):
    pass


class LexiconName(BaseModel):
    __root__: Annotated[str, Field(regex='[0-9A-Za-z]{1,20}')]


class SpeechMarkType(Enum):
    sentence = 'sentence'
    ssml = 'ssml'
    viseme = 'viseme'
    word = 'word'


class TextLengthExceededException(LexiconNotFoundException):
    pass


class InvalidS3BucketException(LexiconNotFoundException):
    pass


class InvalidS3KeyException(LexiconNotFoundException):
    pass


class InvalidSampleRateException(LexiconNotFoundException):
    pass


class InvalidSnsTopicArnException(LexiconNotFoundException):
    pass


class InvalidSsmlException(LexiconNotFoundException):
    pass


class EngineNotSupportedException(LexiconNotFoundException):
    pass


class MarksNotSupportedForFormatException(LexiconNotFoundException):
    pass


class SsmlMarksNotSupportedForTextTypeException(LexiconNotFoundException):
    pass


class LanguageNotSupportedException(LexiconNotFoundException):
    pass


class Alphabet(BaseModel):
    __root__: str


class AudioStream(Alphabet):
    pass


class ContentType(Alphabet):
    pass


class DateTime(BaseModel):
    __root__: datetime


class DeleteLexiconInput(BaseModel):
    pass


class Engine(Enum):
    standard = 'standard'
    neural = 'neural'


class LanguageCode(Enum):
    arb = 'arb'
    cmn_CN = 'cmn-CN'
    cy_GB = 'cy-GB'
    da_DK = 'da-DK'
    de_DE = 'de-DE'
    en_AU = 'en-AU'
    en_GB = 'en-GB'
    en_GB_WLS = 'en-GB-WLS'
    en_IN = 'en-IN'
    en_US = 'en-US'
    es_ES = 'es-ES'
    es_MX = 'es-MX'
    es_US = 'es-US'
    fr_CA = 'fr-CA'
    fr_FR = 'fr-FR'
    is_IS = 'is-IS'
    it_IT = 'it-IT'
    ja_JP = 'ja-JP'
    hi_IN = 'hi-IN'
    ko_KR = 'ko-KR'
    nb_NO = 'nb-NO'
    nl_NL = 'nl-NL'
    pl_PL = 'pl-PL'
    pt_BR = 'pt-BR'
    pt_PT = 'pt-PT'
    ro_RO = 'ro-RO'
    ru_RU = 'ru-RU'
    sv_SE = 'sv-SE'
    tr_TR = 'tr-TR'
    en_NZ = 'en-NZ'
    en_ZA = 'en-ZA'


class IncludeAdditionalLanguageCodes(BaseModel):
    __root__: bool


class NextToken(BaseModel):
    __root__: Annotated[str, Field(max_length=4096, min_length=0)]


class DescribeVoicesInput(BaseModel):
    pass


class EngineList(BaseModel):
    __root__: List[Engine]


class Gender(Enum):
    Female = 'Female'
    Male = 'Male'


class GetLexiconInput(BaseModel):
    pass


class TaskId(BaseModel):
    __root__: Annotated[str, Field(regex='^[a-zA-Z0-9_-]{1,100}$')]


class GetSpeechSynthesisTaskInput(BaseModel):
    pass


class LanguageCodeList(BaseModel):
    __root__: List[LanguageCode]


class LanguageName(Alphabet):
    pass


class LastModified(DateTime):
    pass


class LexemesCount(BaseModel):
    __root__: int


class LexiconContent(BaseModel):
    __root__: SecretStr


class LexiconArn(Alphabet):
    pass


class Size(LexemesCount):
    pass


class LexiconNameList(BaseModel):
    __root__: Annotated[List[LexiconName], Field(max_items=5)]


class ListLexiconsInput(BaseModel):
    pass


class MaxResults(BaseModel):
    __root__: Annotated[int, Field(ge=1.0, le=100.0)]


class TaskStatus(Enum):
    scheduled = 'scheduled'
    inProgress = 'inProgress'
    completed = 'completed'
    failed = 'failed'


class ListSpeechSynthesisTasksInput(BaseModel):
    pass


class OutputFormat(Enum):
    json = 'json'
    mp3 = 'mp3'
    ogg_vorbis = 'ogg_vorbis'
    pcm = 'pcm'


class OutputS3BucketName(BaseModel):
    __root__: Annotated[str, Field(regex='^[a-z0-9][\\.\\-a-z0-9]{1,61}[a-z0-9]$')]


class OutputS3KeyPrefix(BaseModel):
    __root__: Annotated[
        str, Field(regex="^[0-9a-zA-Z\\/\\!\\-_\\.\\*\\'\\(\\):;\\$@=+\\,\\?&]{0,800}$")
    ]


class OutputUri(Alphabet):
    pass


class PutLexiconInput(BaseModel):
    Content: LexiconContent


class RequestCharacters(LexemesCount):
    pass


class SampleRate(Alphabet):
    pass


class SnsTopicArn(BaseModel):
    __root__: Annotated[
        str,
        Field(
            regex='^arn:aws(-(cn|iso(-b)?|us-gov))?:sns:[a-z0-9_-]{1,50}:\\d{12}:[a-zA-Z0-9_-]{1,256}$'
        ),
    ]


class SpeechMarkTypeList(BaseModel):
    __root__: Annotated[List[SpeechMarkType], Field(max_items=4)]


class Text(Alphabet):
    pass


class TextType(Enum):
    ssml = 'ssml'
    text = 'text'


class VoiceId(Enum):
    Aditi = 'Aditi'
    Amy = 'Amy'
    Astrid = 'Astrid'
    Bianca = 'Bianca'
    Brian = 'Brian'
    Camila = 'Camila'
    Carla = 'Carla'
    Carmen = 'Carmen'
    Celine = 'Celine'
    Chantal = 'Chantal'
    Conchita = 'Conchita'
    Cristiano = 'Cristiano'
    Dora = 'Dora'
    Emma = 'Emma'
    Enrique = 'Enrique'
    Ewa = 'Ewa'
    Filiz = 'Filiz'
    Gabrielle = 'Gabrielle'
    Geraint = 'Geraint'
    Giorgio = 'Giorgio'
    Gwyneth = 'Gwyneth'
    Hans = 'Hans'
    Ines = 'Ines'
    Ivy = 'Ivy'
    Jacek = 'Jacek'
    Jan = 'Jan'
    Joanna = 'Joanna'
    Joey = 'Joey'
    Justin = 'Justin'
    Karl = 'Karl'
    Kendra = 'Kendra'
    Kevin = 'Kevin'
    Kimberly = 'Kimberly'
    Lea = 'Lea'
    Liv = 'Liv'
    Lotte = 'Lotte'
    Lucia = 'Lucia'
    Lupe = 'Lupe'
    Mads = 'Mads'
    Maja = 'Maja'
    Marlene = 'Marlene'
    Mathieu = 'Mathieu'
    Matthew = 'Matthew'
    Maxim = 'Maxim'
    Mia = 'Mia'
    Miguel = 'Miguel'
    Mizuki = 'Mizuki'
    Naja = 'Naja'
    Nicole = 'Nicole'
    Olivia = 'Olivia'
    Penelope = 'Penelope'
    Raveena = 'Raveena'
    Ricardo = 'Ricardo'
    Ruben = 'Ruben'
    Russell = 'Russell'
    Salli = 'Salli'
    Seoyeon = 'Seoyeon'
    Takumi = 'Takumi'
    Tatyana = 'Tatyana'
    Vicki = 'Vicki'
    Vitoria = 'Vitoria'
    Zeina = 'Zeina'
    Zhiyu = 'Zhiyu'
    Aria = 'Aria'
    Ayanda = 'Ayanda'


class StartSpeechSynthesisTaskInput(BaseModel):
    Engine: Optional[Engine] = None
    LanguageCode: Optional[LanguageCode] = None
    LexiconNames: Optional[LexiconNameList] = None
    OutputFormat: OutputFormat
    OutputS3BucketName: OutputS3BucketName
    OutputS3KeyPrefix: Optional[OutputS3KeyPrefix] = None
    SampleRate: Optional[SampleRate] = None
    SnsTopicArn: Optional[SnsTopicArn] = None
    SpeechMarkTypes: Optional[SpeechMarkTypeList] = None
    Text: Text
    TextType: Optional[TextType] = None
    VoiceId: VoiceId


class TaskStatusReason(Alphabet):
    pass


class SynthesizeSpeechInput(BaseModel):
    Engine: Optional[Engine] = None
    LanguageCode: Optional[LanguageCode] = None
    LexiconNames: Optional[LexiconNameList] = None
    OutputFormat: OutputFormat
    SampleRate: Optional[SampleRate] = None
    SpeechMarkTypes: Optional[SpeechMarkTypeList] = None
    Text: Text
    TextType: Optional[TextType] = None
    VoiceId: VoiceId


class VoiceName(Alphabet):
    pass


class Voice(BaseModel):
    """
    Description of the voice.
    """

    Gender: Optional[Gender] = None
    Id: Optional[VoiceId] = None
    LanguageCode: Optional[LanguageCode] = None
    LanguageName: Optional[LanguageName] = None
    Name: Optional[VoiceName] = None
    AdditionalLanguageCodes: Optional[LanguageCodeList] = None
    SupportedEngines: Optional[EngineList] = None


class SynthesizeSpeechOutput(BaseModel):
    AudioStream: Optional[AudioStream] = None


class VoiceList(BaseModel):
    __root__: List[Voice]


class Lexicon(BaseModel):
    """
    Provides lexicon name and lexicon content in string format. For more information, see <a href="https://www.w3.org/TR/pronunciation-lexicon/">Pronunciation Lexicon Specification (PLS) Version 1.0</a>.
    """

    Content: Optional[LexiconContent] = None
    Name: Optional[LexiconName] = None


class LexiconAttributes(BaseModel):
    """
    Contains metadata describing the lexicon such as the number of lexemes, language code, and so on. For more information, see <a href="https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html">Managing Lexicons</a>.
    """

    Alphabet: Optional[Alphabet] = None
    LanguageCode: Optional[LanguageCode] = None
    LastModified: Optional[LastModified] = None
    LexiconArn: Optional[LexiconArn] = None
    LexemesCount: Optional[LexemesCount] = None
    Size: Optional[Size] = None


class SynthesisTask(BaseModel):
    """
    SynthesisTask object that provides information about a speech synthesis task.
    """

    Engine: Optional[Engine] = None
    TaskId: Optional[TaskId] = None
    TaskStatus: Optional[TaskStatus] = None
    TaskStatusReason: Optional[TaskStatusReason] = None
    OutputUri: Optional[OutputUri] = None
    CreationTime: Optional[DateTime] = None
    RequestCharacters: Optional[RequestCharacters] = None
    SnsTopicArn: Optional[SnsTopicArn] = None
    LexiconNames: Optional[LexiconNameList] = None
    OutputFormat: Optional[OutputFormat] = None
    SampleRate: Optional[SampleRate] = None
    SpeechMarkTypes: Optional[SpeechMarkTypeList] = None
    TextType: Optional[TextType] = None
    VoiceId: Optional[VoiceId] = None
    LanguageCode: Optional[LanguageCode] = None


class LexiconDescription(BaseModel):
    """
    Describes the content of the lexicon.
    """

    Name: Optional[LexiconName] = None
    Attributes: Optional[LexiconAttributes] = None


class LexiconDescriptionList(BaseModel):
    __root__: List[LexiconDescription]


class SynthesisTasks(BaseModel):
    __root__: List[SynthesisTask]


class DescribeVoicesOutput(BaseModel):
    Voices: Optional[VoiceList] = None
    NextToken: Optional[NextToken] = None


class GetLexiconOutput(BaseModel):
    Lexicon: Optional[Lexicon] = None
    LexiconAttributes: Optional[LexiconAttributes] = None


class GetSpeechSynthesisTaskOutput(BaseModel):
    SynthesisTask: Optional[SynthesisTask] = None


class ListLexiconsOutput(BaseModel):
    Lexicons: Optional[LexiconDescriptionList] = None
    NextToken: Optional[NextToken] = None


class ListSpeechSynthesisTasksOutput(BaseModel):
    NextToken: Optional[NextToken] = None
    SynthesisTasks: Optional[SynthesisTasks] = None


class StartSpeechSynthesisTaskOutput(GetSpeechSynthesisTaskOutput):
    pass
