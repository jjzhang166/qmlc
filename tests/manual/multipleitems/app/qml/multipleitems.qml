/*!
 * Copyright (C) 2014 Nomovok Ltd. All rights reserved.
 * Contact: info@nomovok.com
 *
 * This file may be used under the terms of the GNU Lesser
 * General Public License version 2.1 as published by the Free Software
 * Foundation and appearing in the file LICENSE.LGPL included in the
 * packaging of this file.  Please review the following information to
 * ensure the GNU Lesser General Public License version 2.1 requirements
 * will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
 *
 * In addition, as a special exception, copyright holders
 * give you certain additional rights.  These rights are described in
 * the Digia Qt LGPL Exception version 1.1, included in the file
 * LGPL_EXCEPTION.txt in this package.
 */

import QtQuick 2.0
import "content/testscript1.js" as SS
import CppTests 1.0
import "content"

Item{

    Rectangle {
        id: rect
        width: 200
        height: { return SS.testfunc(width) } // height should be double the width
        color: cppsubitem.color;

        QmlSubItem {
        }

        CppSubItem {
            id: cppsubitem
            color: "blue"
            name: "noname"
        }

        CompositeItem {
        }


        //MouseArea {
        //   anchors.fill: parent;
        //   onClicked: { console.log(cppsubitem.name); }
        //}
    }
}
