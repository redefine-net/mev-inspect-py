from .aave import AAVE_CLASSIFIER_SPECS
from .curve import CURVE_CLASSIFIER_SPECS
from .erc20 import ERC20_CLASSIFIER_SPECS
from .uniswap import UNISWAP_CLASSIFIER_SPECS
from .weth import WETH_CLASSIFIER_SPECS

ALL_CLASSIFIER_SPECS = (
    ERC20_CLASSIFIER_SPECS
    + CURVE_CLASSIFIER_SPECS
    + UNISWAP_CLASSIFIER_SPECS
    + WETH_CLASSIFIER_SPECS
    + AAVE_CLASSIFIER_SPECS
)
