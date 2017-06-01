# Copyright 2016 Google Inc.
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

import third_party.pyperclip as clipboard


clipList = []

def copy(text):
  """Add text onto clipList. Empty |text| is not stored."""
  if text and len(text):
    global clipList
    clipList.append(text)
    if clipboard.copy:
      clipboard.copy(text)

def paste(clipIndex=None):
  """Fetch top of clipList; or clip at index |clipIndex|. The |clipIndex| will
  wrap around if it's larger than the clipList length."""
  if clipIndex is None:
    osClip = clipboard.paste and clipboard.paste()
    if osClip:
      return osClip
    # Get the top of the clipList instead.
    clipIndex = -1
  global clipList
  if len(clipList):
    return clipList[clipIndex%len(clipList)]
  return None