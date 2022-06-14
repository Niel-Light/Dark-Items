class Item():

    def __init__(self, nameValue, physicalDamageValue, magicDamageValue, fireDamageValue, lightningDamageValue, bonusDamageValue, merchantValue):

        self.name = nameValue
        self.physicalDamage = physicalDamageValue
        self.magicDamage = magicDamageValue
        self.fireDamage = fireDamageValue
        self.lightningDamage = lightningDamageValue
        self.bonusDamage = bonusDamageValue
        self.merchant = merchantValue

        @property
        def name(self):
            return self.name

        @property
        def physicalDamage(self):
            return self.physicalDamage

        @property
        def magicDamage(self):
            return self.magicDamage

        @property
        def fireDamage(self):
            return self.fireDamage

        @property
        def lightningDamage(self):
            return self.lightningDamage

        @property
        def bonusDamage(self):
            return self.bonusDamage

        @property
        def merchant(self):
            return self.merchant

        @name.setter
        def name(self, nameValue):
            self.name = nameValue

        @physicalDamage.setter
        def physicalDamage(self, physicalDamageValue):
            self.physicalDamage = physicalDamageValue

        @magicDamage.setter
        def magicDamage(self, magicDamageValue):
            self.magicDamage = magicDamageValue

        @fireDamage.setter
        def fireDamage(self, fireDamageValue):
            self.fireDamage = fireDamageValue

        @lightningDamage.setter
        def lightningDamage(self, lightningDamageValue):
            self.lightningDamage = lightningDamageValue
        
        @bonusDamage.setter
        def bonusDamage(self, bonusDamageValue):
            self.bonusDamage = bonusDamageValue

        @merchant.setter
        def merchant(self, merchantValue):
            self.merchant = merchantValue
