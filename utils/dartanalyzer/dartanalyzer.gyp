# Copyright (c) 2014, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'dartanalyzer',
      'type': 'none',
      'dependencies': [
        '../../runtime/dart-runtime.gyp:dart',
        '../../pkg/pkg.gyp:pkg_packages',
      ],
      'actions': [
        {
          'action_name': 'generate_dartanalyzer_snapshot',
          'inputs': [
            '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)dart<(EXECUTABLE_SUFFIX)',
            '../../sdk/lib/_internal/sdk_library_metadata/lib/libraries.dart',
            '<(SHARED_INTERMEDIATE_DIR)/packages.stamp',
            '<!@(["python", "../../tools/list_files.py", "\\.dart$", "../../pkg/analyzer_cli"])',
            '<!@(["python", "../../tools/list_files.py", "\\.dart$", "../../pkg/analyzer"])',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/dartanalyzer.dart.snapshot',
          ],
          'action': [
            '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)dart<(EXECUTABLE_SUFFIX)',
            '--snapshot=<(SHARED_INTERMEDIATE_DIR)/dartanalyzer.dart.snapshot',
            '--package-root=<(PRODUCT_DIR)/packages/',
            '../../pkg/analyzer_cli/bin/analyzer.dart',
          ],
        },
        {
          'action_name': 'generate_summary_bundle',
          'inputs': [
            '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)dart<(EXECUTABLE_SUFFIX)',
            '<(SHARED_INTERMEDIATE_DIR)/packages.stamp',
            '<!@(["python", "../../tools/list_files.py", "\\.dart$", "../../sdk/lib"])',
            '<!@(["python", "../../tools/list_files.py", "\\.dart$", "../../pkg/analyzer"])',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/sdk_summary_bundle.bin',
          ],
          'action': [
            '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)dart<(EXECUTABLE_SUFFIX)',
            '--package-root=<(PRODUCT_DIR)/packages/',
            '../../pkg/analyzer/tool/summary/build_sdk_summaries.dart',
            'single-output',
            '<(SHARED_INTERMEDIATE_DIR)/sdk_summary_bundle.bin',
          ],
        },
        {
          'action_name': 'extract_spec_summary',
          'inputs': [
            '<(SHARED_INTERMEDIATE_DIR)/sdk_summary_bundle.bin',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/spec.sum',
          ],
          'action': [
            '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)dart<(EXECUTABLE_SUFFIX)',
            '--package-root=<(PRODUCT_DIR)/packages/',
            '../../pkg/analyzer/tool/summary/build_sdk_summaries.dart',
            'extract-spec-sum',
            '<(SHARED_INTERMEDIATE_DIR)/sdk_summary_bundle.bin',
            '<(SHARED_INTERMEDIATE_DIR)/spec.sum',
          ],
        },
        {
          'action_name': 'extract_strong_summary',
          'inputs': [
            '<(SHARED_INTERMEDIATE_DIR)/sdk_summary_bundle.bin',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/strong.sum',
          ],
          'action': [
            '<(PRODUCT_DIR)/<(EXECUTABLE_PREFIX)dart<(EXECUTABLE_SUFFIX)',
            '--package-root=<(PRODUCT_DIR)/packages/',
            '../../pkg/analyzer/tool/summary/build_sdk_summaries.dart',
            'extract-strong-sum',
            '<(SHARED_INTERMEDIATE_DIR)/sdk_summary_bundle.bin',
            '<(SHARED_INTERMEDIATE_DIR)/strong.sum',
          ],
        },
      ],
    },
  ],
}
