# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
# Copyright 2022 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# flake8: noqa

import os

from packaging import version

from ..version import VERSION as __version__
from .deprecation_utils import deprecate
from .import_utils import (
    ENV_VARS_TRUE_AND_AUTO_VALUES,
    ENV_VARS_TRUE_VALUES,
    USE_PADDLE,
    DummyObject,
    OptionalDependencyNotAvailable,
    is_fastdeploy_available,
    is_inflect_available,
    is_k_diffusion_available,
    is_librosa_available,
    is_modelcards_available,
    is_onnx_available,
    is_paddle_available,
    is_paddle_version,
    is_paddlenlp_available,
    is_scipy_available,
    is_unidecode_available,
    requires_backends,
)
from .logging import get_logger
from .outputs import BaseOutput
from .pil_utils import PIL_INTERPOLATION

if is_paddle_available():
    from .testing_utils import (
        floats_tensor,
        image_grid,
        load_hf_numpy,
        load_image,
        load_numpy,
        load_ppnlp_numpy,
        nightly,
        paddle_all_close,
        parse_flag_from_env,
        slow,
    )

logger = get_logger(__name__)

from paddlenlp.utils.env import _get_ppnlp_home, _get_sub_home

ppnlp_cache_home = _get_ppnlp_home()
default_cache_path = _get_sub_home("models")

CONFIG_NAME = "config.json"
WEIGHTS_NAME = "model_state.pdparams"
FASTDEPLOY_WEIGHTS_NAME = "inference.pdiparams"
FASTDEPLOY_MODEL_NAME = "inference.pdmodel"
DOWNLOAD_SERVER = "https://bj.bcebos.com/paddlenlp/models/community"
PPDIFFUSERS_CACHE = default_cache_path
PPDIFFUSERS_DYNAMIC_MODULE_NAME = "ppdiffusers_modules"
PPNLP_MODULES_CACHE = os.getenv("PPNLP_MODULES_CACHE", _get_sub_home("modules"))
HF_CACHE = os.environ.get("HUGGINGFACE_HUB_CACHE", PPDIFFUSERS_CACHE)
TEST_DOWNLOAD_SERVER = "https://paddlenlp.bj.bcebos.com/models/community/ppdiffusers/tests"

_COMPATIBLE_STABLE_DIFFUSION_SCHEDULERS = [
    "DDIMScheduler",
    "DDPMScheduler",
    "PNDMScheduler",
    "LMSDiscreteScheduler",
    "EulerDiscreteScheduler",
    "HeunDiscreteScheduler",
    "EulerAncestralDiscreteScheduler",
    "DPMSolverMultistepScheduler",
    "DPMSolverSinglestepScheduler",
]


def check_min_version(min_version):
    if version.parse(__version__) < version.parse(min_version):
        if "dev" in min_version:
            error_message = "This example requires a source install from ppdiffusers"
        else:
            error_message = f"This example requires a minimum version of {min_version},"
        error_message += f" but the version found is {__version__}.\n"
        raise ImportError(error_message)
