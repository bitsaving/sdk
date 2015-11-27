// Copyright (c) 2015, the Dart project authors.  Please see the AUTHORS file
// for details. All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.

/**
 * Support for client code that extends the analysis server by adding new code
 * Dart specific completion contributors.
 *
 * Plugins can register Dart specific completion contributor factories.
 * The registered contributor factoriess will be used to instantiate new
 * contributors to get completions any time a client issues
 * a 'completion.getSuggestions' request.
 *
 * If a plugin wants to add completions, it should implement the class
 * [DartCompletionContributorFactory] and then register the contributor
 * by including code like the following in the plugin's
 * registerExtensions method:
 *
 *     @override
 *     void registerExtensions(RegisterExtension registerExtension) {
 *       ...
 *       registerExtension(
 *           DART_COMPLETION_CONTRIBUTOR_EXTENSION_POINT_ID,
 *           () => [new MyDartCompletionContributor()]);
 *       ...
 *     }
 */
library analysis_server.src.provisional.completion.completion;

import 'package:analysis_server/src/plugin/server_plugin.dart';
import 'package:analysis_server/src/provisional/completion/dart/completion_dart.dart';
import 'package:plugin/plugin.dart';

/**
 * The identifier of the extension point that allows plugins to register code
 * completion contributors. The object used as an extension must be a
 * [DartCompletionContributor].
 */
final String DART_COMPLETION_CONTRIBUTOR_EXTENSION_POINT_ID = Plugin.join(
    ServerPlugin.UNIQUE_IDENTIFIER,
    ServerPlugin.DART_COMPLETION_CONTRIBUTOR_EXTENSION_POINT);