# menuTitle: Name Record Editor
# 27.07.2024 Ryan Bugden helped me for the layout on discord channel
# https://discord.com/channels/1052516637489766411/1266757838781419672/1266767558745395200

import ezui

class NameRecordEditor(ezui.WindowController):

    def build(self):
        content = """
        |--------------------------------------------------------|
        | nameID | platformID | encodingID | languageID | string | @complexTable
        |--------|------------|------------|------------|--------|
        |        |            |            |            |        |
        |        |            |            |            |        |
        |--------------------------------------------------------|
        > (+-)    @complexTableAddRemoveButton
        > (Apply Changes to All Fonts) @complexTablePrintButton
        """
        complexTableItems = [
            dict(
                nameID="",
                platformID="",
                encodingID="1",
                languageID="0x0409",
                string=""
            )
        ]

        descriptionData = dict(
            complexTable=dict(
                width="auto",
                items=complexTableItems,
                columnDescriptions=[
                    dict(
                        identifier="nameID",
                        title="Name ID",
                        width=70,
                        editable=True
                    ),
                    dict(
                        identifier="platformID",
                        title="Platform ID",
                        width=70,
                        cellDescription=dict(
                            valueType="string"
                        ),
                        editable=True
                    ),
                    dict(
                        identifier="encodingID",
                        title="Encoding ID",
                        width=70,
                        editable=True
                    ),
                    dict(
                        identifier="languageID",
                        title="Language ID",
                        width=70,
                        editable=True
                    ),
                    dict(
                        identifier="string",
                        title="String",
                        width=85,
                        editable=True
                    ),
                ]
            )
        )
        self.w = ezui.EZPanel(
            title="Name Record Editor",
            size=(500, 200),
            content=content,
            descriptionData=descriptionData,
            controller=self
        )

    def started(self):
        self.w.open()
        
    def parse_int(self, value):
        try:
            # Check if the value starts with '0x' for hexadecimal
            if value.startswith('0x'):
                return int(value, 16)  # Convert from hexadecimal
            else:
                return int(value)  # Convert from decimal
        except ValueError:
            print(f"Invalid integer value: {value}")
            return None

    def applyChangesCallback(self, sender):
        table = self.w.getItem("complexTable")
        records = table.get()

        newRecords = []
        for record in records:
            desired_nameID = self.parse_int(record["nameID"])
            desired_platformID = self.parse_int(record["platformID"])
            desired_encodingID = self.parse_int(record["encodingID"])
            desired_languageID = self.parse_int(record["languageID"])
            desired_string = record["string"]

            if None in (desired_nameID, desired_platformID, desired_encodingID, desired_languageID):
                print("Error: One or more fields have invalid values.")
                return

            newRecords.append({
                "nameID": desired_nameID,
                "platformID": desired_platformID,
                "encodingID": desired_encodingID,
                "languageID": desired_languageID,
                "string": desired_string
            })

        for font in AllFonts():
            # Access the font info
            info = font.info

            # Initialize openTypeNameRecords if it does not exist
            if info.openTypeNameRecords is None:
                info.openTypeNameRecords = []

            # Update or add the new name records
            self.updateOrAddRecords(info.openTypeNameRecords, newRecords)

            font.changed()
        print("Updated Name Record Format for all open UFOs.")

    def updateOrAddRecords(self, records, newRecords):
        for newRecord in newRecords:
            found = False
            for index, record in enumerate(records):
                if (record["nameID"] == newRecord["nameID"] and
                        record["platformID"] == newRecord["platformID"] and
                        record["languageID"] == newRecord["languageID"]):
                    # Update existing record
                    records[index] = newRecord
                    found = True
                    break
            if not found:
                # Add new record if not found
                records.append(newRecord)

    def complexTableAddRemoveButtonAddCallback(self, sender):
        table = self.w.getItem("complexTable")
        item = table.makeItem(
            encodingID="1",
            languageID="0x0409"
        )
        table.appendItems([item])

    def complexTableAddRemoveButtonRemoveCallback(self, sender):
        table = self.w.getItem("complexTable")
        table.removeSelectedItems()

    def complexTablePrintButtonCallback(self, sender):
        self.applyChangesCallback(sender)

NameRecordEditor()