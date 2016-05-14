/**
 * @author    Lien Mergan based on an example of Olivier Parent
 * @copyright Copyright © 2015-2016 Artevelde University College Ghent
 * @license   Apache License, Version 2.0
 */

;(function () {
    'use strict';

    var secure = false;

    angular.module('app')
        .constant('config', {
            api: {
                protocol: secure ? 'https' : 'http',
                host    : '127.0.0.1:8000',
                path    : '/www/api'
            }
        });
})();
