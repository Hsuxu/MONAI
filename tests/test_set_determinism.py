# Copyright 2020 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import torch
import numpy as np
from monai.utils import set_determinism, get_seed


class TestSetDeterminism(unittest.TestCase):
    def test_values(self):
        seed = 255
        set_determinism(seed=seed)
        self.assertEqual(seed, get_seed())
        a = np.random.randint(seed)
        b = torch.randint(seed, (1,))
        set_determinism(seed=seed)
        c = np.random.randint(seed)
        d = torch.randint(seed, (1,))
        self.assertEqual(a, c)
        self.assertEqual(b, d)


if __name__ == "__main__":
    unittest.main()
