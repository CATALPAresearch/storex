import datasets
import json

logger = datasets.logging.get_logger(__name__)
_VERSION = "1.0"
_NAME = "qg_oop"
_DESCRIPTION = """German SQuAD-inspired dataset for questions regarding object-oriented programming."""
URL = 'https://huggingface.co/datasets/LunaticTanuki/qg_OOP/resolve/main/processed'
_URLS = {
    'train': ['{}/train.jsonl'.format(URL)],
    'validation': ['{}/validation.jsonl'.format(URL)]
}


class QGSquadConfig(datasets.BuilderConfig):
    """BuilderConfig for SquadQG"""

    def __init__(self, **kwargs):
        """BuilderConfig for SquadQG.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(QGSquadConfig, self).__init__(**kwargs)


class QGSquad(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        QGSquadConfig(name=_NAME, version=datasets.Version(_VERSION), description=_DESCRIPTION),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "answer": datasets.Value("string"), "paragraph_question": datasets.Value("string"),
                    "question": datasets.Value("string"),
                    "sentence": datasets.Value("string"),
                    "paragraph": datasets.Value("string"),
                    "sentence_answer": datasets.Value("string"),
                    "paragraph_answer": datasets.Value("string"),
                    "paragraph_sentence": datasets.Value("string")
                }
            ),
            supervised_keys=None,
            # homepage="https://github.com/asahi417/lm-question-generation"
        )

    def _split_generators(self, dl_manager):
        downloaded_file = dl_manager.download_and_extract(_URLS)
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepaths": downloaded_file["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION,
                                    gen_kwargs={"filepaths": downloaded_file["validation"]}),
            # datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepaths": downloaded_file["test"]}),
        ]

    def _generate_examples(self, filepaths):
        _key = 0
        for filepath in filepaths:
            logger.info("generating examples from = %s", filepath)
            with open(filepath, encoding="utf-8") as f:
                _list = f.read().split('\n')
                if _list[-1] == '':
                    _list = _list[:-1]
                for i in _list:
                    data = json.loads(i)
                    yield _key, data
                    _key += 1
