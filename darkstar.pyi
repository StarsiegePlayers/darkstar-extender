
def currentInstance() -> Game: ...

class Game:
    class Core:
        def loadObject(self): ...

        def storeObject(self): ...

        def deleteObject(self): ...

        def isObject(self): ...

        def isFile(self): ...

        def listVolumes(self): ...

        def listObjects(self): ...

        def newObject(self): ...

        def addToSet(self): ...

        def postAction(self): ...

        def focus(self): ...

        def unfocus(self): ...

        def purgeResources(self): ...

        def focusClient(self): ...

        def focusServer(self): ...

        def newClient(self): ...

        def newServer(self): ...

        def deleteClient(self): ...

        def deleteServer(self): ...

        def remoteEval(self): ...

        def inspectObject(self): ...

        def renameObject(self): ...

        def setObjectId(self): ...

        def schedule(self): ...

        def getSimTime(self): ...

        def setWindowTitle(self): ...

        def getPathOf(self): ...

        def getGroup(self): ...

        def isMember(self): ...

        def getNextObject(self): ...

    @property
    def core(self) -> Core: ...

    @property
    def console(self) -> Console: ...

    @property
    def knownPlugins(self) -> KnownPlugins: ...


class Console:
    def cls(self): ...

    def floor(self): ...

    def sqrt(self): ...

    def echo(self): ...

    def dbecho(self): ...

    def strcat(self): ...

    def quit(self): ...

    def export(self): ...

    def deleteVariables(self): ...

    def exportFunctions(self): ...

    def deleteFunctions(self): ...

    def exec(self): ...

    def eval(self): ...

    def debug(self): ...

    def trace(self): ...


class KnownPlugins:
    @property
    def guiConsole(self) -> SimGuiConsolePlugin: ...

    @property
    def gfx(self) -> GFXPlugin: ...

    @property
    def terrain(self) -> TerrainPlugin: ...

    @property
    def interior(self) -> InteriorPlugin: ...

    @property
    def sky(self) -> SkyPlugin: ...

    @property
    def net(self) -> NetPlugin: ...

    @property
    def soundFx(self) -> SoundFXPlugin: ...

    @property
    def redbook(self) -> RedbookPlugin: ...

    @property
    def movPlay(self) -> MovPlayPlugin: ...

    @property
    def input(self) -> SimInputPlugin: ...

    @property
    def gui(self) -> SimGuiPlugin: ...

    @property
    def tool(self) -> ToolPlugin: ...

    @property
    def tree(self) -> SimTreePlugin: ...

    @property
    def mission(self) -> MissionPlugin: ...

    @property
    def fearMission(self) -> FearMissionPlugin: ...

    @property
    def gameplay(self) -> ESGameplayPlugin: ...

    @property
    def shell(self) -> ShellOpenPlugin: ...

    @property
    def landscape(self) -> ShellOpenPlugin: ...

    @property
    def ted(self) -> ShellOpenPlugin: ...

    @property
    def winConsole(self) -> ShellOpenPlugin: ...

    @property
    def telnet(self) -> SimTelnetPlugin: ...

    @property
    def shape(self) -> SimShapePlugin: ...

    @property
    def hercInfo(self) -> HercInfoDataPlugin: ...

    @property
    def database(self) -> DatabasePlugin: ...

    @property
    def inputControl(self) -> ICPlugin: ...

    @property
    def irc(self) -> IRCPlugin: ...

    @property
    def esf(self) -> ESFPlugin: ...

    @property
    def base(self) -> ESBasePlugin: ...

    @property
    def chat(self) -> ESChatPlugin: ...

    @property
    def dynamicData(self) -> DynamicDataPlugin: ...


class SimGuiConsolePlugin:
    def consoleEnable(self): ...

class GFXPlugin:
    def swapSurfaces(self): ...

    def isFullscreenMode(self): ...

    def setFullscreenMode(self): ...

    def setFSResolution(self): ...

    def isVirtualFS(self): ...

    def nextRes(self): ...

    def prevRes(self): ...

    def screenShot(self, name = None): ...

    def setScreenShotSeq(self, sequence): ...

    def flushTextureCache(self, ): ...

    def resetUpdateRegion(self): ...

    def setGamma(self, simCanvasName: str, gammaValue: float): ...

    def setFullscreenDevice(self, simCanvasName: str, deviceName: str): ...

    def setWindowedDevice(self, simCanvasName: str, deviceName: str): ...

    def listDevices(self): ...

    def testDevice(self, deviceName) -> bool: ...

    def messageCanvasDevice(self, simCanvasName: str, message: str): ...

    def setWindowSize(self, simCanvasName: str, width: int, height: int): ...

    def lockWindowSize(self, simCanvasName: str): ...

    def unlockWindowSize(self, simCanvasName: str): ...

    def isGfxDriver(self, simCanvasName: str, driverName: str): ...

class TerrainPlugin:
    def newTerrain(self): ...

    def newTerrainParam(self): ...

    def loadTerrain(self): ...

    def saveTerrain(self, objectName: str, volumeName: str): ...

    def setTerrainVisibility(self, objectName: str, visibleDist: str, hazeDist: int): ...

    def setTerrainDetail(self, objectName: str, perspectiveDist: int, screenSquareSize: int): ...

    def setTerrainContainer(self, objectName: str, gravity: int, drag: int, height: int): ...

    def lightTerrain(self, objectName: str, minX: int = None, minY: int = None, maxX: int = None, maxY: int = None): ...

    def showTerrain(self, terrainOn: bool = None): ...

class InteriorPlugin:
    def setITRShapeState(self, objectName: str, stateNumber: int): bool: ...

    def setITRLightState(self, objectName: str, stateNumber: int): bool: ...

    def animateInteriorLight(self, interiorObjectName: str, lightName: str, loopCount: int): bool: ...

    def stopInteriorLightAnim(self, interiorObjectName: str, lightName: str): bool: ...

    def resetInteriorLight(self, interiorObjectName: str, lightName: str): bool: ...

    def ITR__toggleBoundingBox(self): bool: ...

class SkyPlugin:
    def globeLines(self): ...

    def showLowerStars(self, shouldShow: bool = None): ...

    def setStarsVisibility(self, shouldShow: bool = None): ...

    def setSkyMaterialListTag(self, tag: int): ...


class NetPlugin:
    def netStats(self): ...

    def logPacketStats(self): ...

    def DNet__TranslateAddress(self, source: str, timeout: int = 0): ...

    def playDemo(self, filename: str): ...

    def timeDemo(self, filename: str): ...

    def connect(self, netAddress: str): ...

    def disconnect(self): ...

    def net__kick(self, playerId: int, reason: str = None): ...

class SoundFXPlugin:
    def newSfx(self) -> bool: ...

    def sfxOpen(self) -> bool: ...

    def sfxClose(self) -> bool: ...

    def sfxQuery(self, driverId) -> bool: ...

    def sfxAdd2DProfile(self, profileId: int, baseVolume: float, flags: list): ...

    def sfxAdd3DProfile(self, profileId: int, baseVolume: float, minDist: float, maxDist: float, coneVolume: float = None, coneInside: float = None, coneOutside: float = None, vectorX: float = None, vectorY: float = None, vectorZ: float = None, flags: list = None): ...

    def sfxAddPair(self, pairId: int, profileId: int, wavName: str, priority: float): ...

    def sfxRemoveProfile(self): ...

    def sfxRemovePair(self): ...

    def sfxPlay(self, handleId: int): ...

    def sfxStop(self, handleId: int): ...

    def sfxMute(self, shouldMute = True): ...

    def sfxSetPosition(self, handleId: int, x: int, y: int, z: int): ...

    def sfxSetPan(self, handleId: int, pan: float): ...

    def sfxSetListenerPosition(self, x, y, z): ...

    def sfxSetFormat(self, frequence: int, bitDepth: int, stereo: bool) -> bool: ...

    def sfxGetFormat(self) -> bool: ...

    def sfxSetVolume(self, volume: float, handleId: int): ...

    def sfxSetMaxBuffers(self, bufferCount: int): ...

    def sfxGetMaxBuffers(self): ...

# TODO finish this
class RedbookPlugin:
    def newRedbook(self): ...

    def rbOpen(self): ...

    def rbEject(self): ...

    def rbRetract(self): ...

    def rbGetStatus(self): ...

    def rbGetTrackCount(self): ...

    def rbGetTrackInfo(self): ...

    def rbGetTrackPosition(self): ...

    def rbPlay(self): ...

    def rbStop(self): ...

    def rbPause(self): ...

    def rbResume(self): ...

    def rbSetVolume(self): ...

    def rbGetVolume(self): ...

    def rbSetPlayMode(self): ...


# TODO finish this
class MovPlayPlugin:
    def newMovPlay(self): ...

    def openMovie(self): ...

    def closeMovie(self): ...

    def playMovie(self): ...

    def playMovieToComp(self): ...

    def stopMovie(self): ...

    def pauseMovie(self): ...

# TODO finish this
class SimInputPlugin:
    def newInputManager(self): ...

    def listInputDevices(self): ...

    def getInputDeviceInfo(self): ...

    def saveInputDeviceInfo(self): ...

    def inputOpen(self): ...

    def inputClose(self): ...

    def inputCapture(self): ...

    def inputRelease(self): ...

    def inputActivate(self): ...

    def inputDeactivate(self): ...

    def editActionMap(self): ...

    def newActionMap(self): ...

    def bindAction(self): ...

    def bindCommand(self): ...

    def bind(self): ...

    def saveActionMap(self): ...


# TODO finish this
class SimGuiPlugin:
    def GuiEditMode(self): ...

    def GuiEditNewControl(self): ...

    def GuiSetAddSet(self): ...

    def GuiSetSelection(self): ...

    def GuiNewContentCtrl(self): ...

    def GuiLoadContentCtrl(self): ...

    def GuiSaveContentCtrl(self): ...

    def GuiSaveSelection(self): ...

    def GuiLoadSelection(self): ...

    def GuiInspect(self): ...

    def GuiJustify(self): ...

    def GuiToolbar(self): ...

    def GuiSendToBack(self): ...

    def GuiBringToFront(self): ...

    def GuiSendRootMessage(self): ...

    def setCursor(self): ...

    def isCursorOn(self): ...

    def cursorOn(self): ...

    def cursorOff(self): ...

    def windowsMouseEnable(self): ...

    def windowsMouseDisable(self): ...

    def GuiPushDialog(self): ...

    def GuiPopDialog(self): ...

    class GuiControl:
        def performClick(self): ...

        def setValue(self): ...

        def getValue(self): ...

        def setActive(self): ...

        def getActive(self): ...

        def setVisible(self): ...

        def getVisible(self): ...

        def setText(self): ...

        def getText(self): ...

    @property
    def control(self) -> GuiControl: ...

    class GuiTextList:
        def clear(self): ...

        def addLine(self): ...

    @property
    def textList(self) -> GuiTextList: ...

    class GuiEdit:
        @property
        def gridSnapX(self): ...

        @property
        def gridSnapY(self): ...

    @property
    def guiEdit(self) -> GuiTextList: ...

# TODO finish this
class ToolPlugin:
    def newToolWindow(self): ...

    def newToolStrip(self): ...

    def listToolButtons(self): ...

    def listToolWindows(self): ...

    def hideToolWin(self): ...

    def showToolWin(self): ...

    def showToolWinAll(self): ...

    def hideToolWinAll(self): ...

    def setToolWinPos(self): ...

    def addToolButton(self): ...

    def delToolButton(self): ...

    def addToolGap(self): ...

    def setToolCommand(self): ...

    def setButtonHelp(self): ...

    def isButtonDown(self): ...

    def addStatusBar(self): ...

    def delStatusBar(self): ...

    def setStatusField(self): ...

    def getStatusField(self): ...

    def clearStatusField(self): ...

    def setMainWindow(self): ...

    def editBox(self): ...

    def browseBox(self): ...

    def edit2Box(self): ...

    def confirmBox(self): ...

    def openFile(self): ...

    def saveFileAs(self): ...

# TODO finish this
class SimTreePlugin:
    def simTreeCreate(self): ...

    def simTreeAddSet(self): ...

    def simTreeRegBitmaps(self): ...

    def simTreeRegClass(self): ...

    def simTreeRegScript(self): ...

# TODO finish this
class MissionPlugin:
    def MissionEditor(self): ...

    def MissionRegType(self): ...

    def MissionRegObject(self): ...

    def MissionRegTerrain(self): ...

    def MissionCreateObject(self): ...

    def MissionAddObject(self): ...

    def MissionLoadObjects(self): ...

    def newMissionGroup(self): ...

    def addMissionButton(self): ...

    def removeMissionButton(self): ...

    def removeMissionButtons(self): ...

    def setMissionButtonChecked(self): ...

    def setMissionButtonEnabled(self): ...

    def isMissionButtonChecked(self): ...

    def isMissionButtonEnabled(self): ...

    def missionSetAutoSaveInterval(self): ...

    def missionSetAutoSaveName(self): ...

    def missionSaveObjectPersist(self): ...

    def missionLoadObjectPersist(self): ...

    def missionUndoMoveRotate(self): ...

# TODO finish this
class FearMissionPlugin:
    class MissionEditor:
        def Create(self): ...

        def RegisterType(self): ...

        def SetGrabMask(self): ...

        def SetPlaceMask(self): ...

        def SetDefaultPlaceMask(self): ...

        def GetConsoleOptions(self): ...

        def ObjectToCamera(self): ...

        def CameraToObject(self): ...

        def ObjectToSC(self): ...

        def onSelected(self): ...

        def onUnselected(self): ...

        def onSelectionCleared(self): ...

        def onUseTerrainGrid(self): ...

        def DeleteSelection(self): ...

        def CopySelection(self): ...

        def CutSelection(self): ...

        def PasteSelection(self): ...

        def PasteFile(self): ...

        def DuplicateSelection(self): ...

        def CreateGroup(self): ...

        def DropSelection(self): ...

        def PlaceBookmark(self): ...

        def GotoBookmark(self): ...

        def Undo(self): ...

        def Redo(self): ...

        def Save(self): ...

        def MissionLight(self): ...

        def RebuildCommandMap(self): ...

    @property
    def me(self) -> MissionEditor: ...

    def MissionCreateObject(self): ...


# TODO finish this
class ESGameplayPlugin:
    def goto(self): ...

    def drop(self): ...

    def redrop(self): ...

    def fov(self): ...

    def nightvision(self): ...

    def order(self): ...

    def orderSquadMate(self): ...

    def collisionDetail(self): ...

    def cloneVehicle(self): ...

    def setVehicleSpecialIdentity(self): ...

    def addVehicleMass(self): ...

    def setShapeVisibility(self): ...

    def getVehicleName(self): ...

    def getVehicleAvailableMass(self): ...

    def setTurretOwner(self): ...

    def setHercOwner(self): ...

    def setPilotId(self): ...

    def setVehicleRadarVisible(self): ...

    def setCombatCamera(self): ...

    def setDominantCamera(self): ...

    def setFlybyCamera(self): ...

    def setTowerCamera(self): ...

    def setPlayerCamera(self): ...

    def setOrbitCamera(self): ...

    def cameraLockFocus(self): ...

    def orbitPlayer(self): ...

    def combatCamera(self): ...

    def targetPrimaryCamera(self): ...

    def targetSecondaryCamera(self): ...

    def freeLookCamera(self): ...

    def flybyCamera(self): ...

    def towerCamera(self): ...

    def getComponentCount(self): ...

    def getComponentId(self): ...

    def getWeaponCount(self): ...

    def getWeaponId(self): ...

    def forceScope(self): ...

    def getTargetId(self): ...

    def dumpDamage(self): ...

    def getTerrainHeight(self): ...

    def forceCommandPopup(self): ...

    def componentIsInPlanetInventory(self): ...

    def weaponIsInPlanetInventory(self): ...

    def localNavIgnoreObject(self): ...

    def localNavIgnoreEverythin(self): ...

    def getVehicleTechBase(self): ...

    def violate(self): ...

# TODO finish this
class ShellOpenPlugin:
    def HTMLOpen(self): ...

    def HTMLOpenAndGoWin(self): ...

# TODO finish this
class LSPlugin:
    class Landscaper:
        def Create(self): ...

        def Rules(self): ...

        def Textures(self): ...

        def Script(self): ...

        def ApplyTextures(self): ...

        def ApplyLandScape(self): ...

        def Editor(self): ...

        def flushTextures(self): ...

        def addTerrainTexture(self): ...

        def addTerrainType(self): ...

        def createGridFile(self): ...

        def flushRules(self): ...

        def addRule(self): ...

        def flushCommands(self): ...

        def addCommand(self): ...

        def parseCommands(self): ...

    @property
    def ls(self) -> Landscaper: ...

# TODO finish this
class TedPlugin:
    def initTed(self): ...

    def quitTed(self): ...

    def attachToTerrain(self): ...

    def setSnap(self): ...

    def setFeather(self): ...

    def setSelectFrameColor(self): ...

    def setSelectFillColor(self): ...

    def setHilightFrameColor(self): ...

    def setHilightFillColor(self): ...

    def setShadowFrameColor(self): ...

    def setShadowFillColor(self): ...

    def setSelectShow(self): ...

    def setHilightShow(self): ...

    def setShadowShow(self): ...

    def setBlockOutline(self): ...

    def setBlockFrameColor(self): ...

    def setBrushPos(self): ...

    def setLButtonAction(self): ...

    def setRButtonAction(self): ...

    def getLButtonActionIndex(self): ...

    def getRButtonActionIndex(self): ...

    def relight(self): ...

    def clearSelect(self): ...

    def undo(self): ...

    def redo(self): ...

    def setBrushDetail(self): ...

    def setPinDetailVal(self): ...

    def setPinDetailMax(self): ...

    def setHeightVal(self): ...

    def setAdjustVal(self): ...

    def setFlagVal(self): ...

    def setScaleVal(self): ...

    def processAction(self): ...

    def terrainAction(self): ...

    def setFlags(self): ...

    def clearFlags(self): ...

    def toggleFlags(self): ...

    def rotate(self): ...

    def setUndoLimit(self): ...

    def listCommands(self): ...

    def addNamedSelection(self): ...

    def removeNamedSelection(self): ...

    def selectNamedSelection(self): ...

    def copy(self): ...

    def paste(self): ...

    def selectMaterial(self): ...

    def focus(self): ...

    def unfocus(self): ...

    def forceTerrainType(self): ...

    def setTerrainType(self): ...

    def getTerrainType(self): ...

    def setSmoothVal(self): ...

    def setPasteVal(self): ...

    def clearPinMaps(self): ...

    def getBrushDetail(self): ...

    def getMaxBrushDetail(self): ...

    def getNumTerrainTypes(self): ...

    def getTerrainTypeName(self): ...

    def loadPalette(self): ...

    def assignMatList(self): ...

    def loadMatList(self): ...

    def getMaterialCount(self): ...

    def getMaterialName(self): ...

    def getMaterialIndex(self): ...

    def new(self): ...

    def open(self): ...

    def close(self): ...

    def save(self): ...

    def setMatIndexVal(self): ...

    def listNamedSelections(self): ...

    def updateToolBar(self): ...

    def window(self): ...

    def setStatusText(self): ...

    def saveSelection(self): ...

    def loadSelection(self): ...

    def GetConsoleOptions(self): ...

    def getNumActions(self): ...

    def getActionName(self): ...

    def isActionMouseable(self): ...

    def floatSelection(self): ...

    def floatPaste(self): ...

    def mirrorGridBlock(self): ...

    def getWorldName(self): ...

# TODO finish this
class SimWinConsolePlugin:
    @property
    def WinConsoleEnabled(self): ...

    @property
    def dedicated(self): ...

# TODO finish this
class SimTelnetPlugin:
    @property
    def TelnetPort(self): ...

# TODO finish this
class SimShapePlugin:
    class SimShape:
        def toggleBoundingBox(self): ...

    @property
    def simShape(self) -> SimShape: ...


# TODO finish this
class HercInfoDataPlugin:
    def defaultWeapons(self): ...

    def defaultMountables(self): ...

    def newHerc(self): ...

    def harcBase(self): ...

    def hercPos(self): ...

    def hercPos(self): ...

    def hercRot(self): ...

    def hercAnim(self): ...

    def hercFootprint(self): ...

    def hercCpit(self): ...

    def herColl(self): ...

    def hercAi(self): ...

    def vehiclePilotable(self): ...

    def newTank(self): ...

    def tankBase(self): ...

    def tankPos(self): ...

    def tankRot(self): ...

    def tankCpit(self): ...

    def tankColl(self): ...

    def tankAnim(self): ...

    def tankSound(self): ...

    def tankSlide(self): ...

    def tankAi(self): ...

    def vehicleArtillery(self): ...

    def newDrone(self): ...

    def droneBase(self): ...

    def dronePos(self): ...

    def droneRot(self): ...

    def droneColl(self): ...

    def droneAnim(self): ...

    def droneSound(self): ...

    def droneSlide(self): ...

    def droneExplosion(self): ...

    def newFlyer(self): ...

    def flyerBase(self): ...

    def flyerPos(self): ...

    def flyerRot(self): ...

    def flyerCpit(self): ...

    def flyerColl(self): ...

    def flyerExhaust(self): ...

    def flyerExhaustOffset(self): ...

    def flyerAi(self): ...

    def flyerNav(self): ...

    def flyerSound(self): ...

    def translucentCockpit(self): ...

    def newTurret(self): ...

    def turretBase(self): ...

    def turretAi(self): ...

    def newHardpoint(self): ...

    def newMountPoint(self): ...

    def newHardpointExt(self): ...

    def hardpointSpecial(self): ...

    def hardpointDamage(self): ...

    def newComponent(self): ...

    def newConfiguration(self): ...

    def newWeapon(self): ...

    def weaponInfo1(self): ...

    def weaponInfo2(self): ...

    def weaponMuzzle(self): ...

    def weaponGeneral(self): ...

    def weaponShot(self): ...

    def weaponAmmo(self): ...

    def weaponEnergy(self): ...

    def newBullet(self): ...

    def newMissile(self): ...

    def newEnergy(self): ...

    def newBeam(self): ...

    def newMine(self): ...

    def newBomb(self): ...

    def newMountable(self): ...

    def mountInfo1(self): ...

    def mountInfo2(self): ...

    def newEngine(self): ...

    def engineInfo1(self): ...

    def engineInfo2(self): ...

    def newSensor(self): ...

    def sensorInfo1(self): ...

    def sensorInfo2(self): ...

    def sensorMode(self): ...

    def sensorMode(self): ...

    def newReactor(self): ...

    def reactorInfo1(self): ...

    def reactorInfo2(self): ...

    def newShield(self): ...

    def shieldInfo1(self): ...

    def shieldInfo2(self): ...

    def newModulator(self): ...

    def newAmplifier(self): ...

    def newCapacitor(self): ...

    def newComputer(self): ...

    def newBooster(self): ...

    def newRepair(self): ...

    def newCloak(self): ...

    def cloakInfo1(self): ...

    def cloakInfo2(self): ...

    def newArmor(self): ...

    def armorInfo1(self): ...

    def armorInfo2(self): ...

    def armorInfoSpecial(self): ...

    def newEcm(self): ...

    def newThermal(self): ...

    def newBattery(self): ...

    def newFormation(self): ...

    def inventoryComponentSet(self): ...

    def inventoryComponentAdjust(self): ...

    def inventoryWeaponSet(self): ...

    def inventoryWeaponAdjust(self): ...

    def inventoryVehicleSet(self): ...

    def inventoryVehicleAdjust(self): ...

    def inventoryPilotSet(self): ...

    def inventoryList(self): ...

    def getPlanet(self): ...

    def addComponentToPlanetSalvage(self): ...

    def addWeaponToPlanetSalvage(self): ...

    def addComponentToStashSalvage(self): ...

    def addWeaponToStashSalvage(self): ...

    def allowVehicle(self): ...

    def allowComponent(self): ...

    def allowWeapon(self): ...

# TODO finish this
class DatabasePlugin:
    def dataStore(self): ...

    def dataRetrieve(self): ...

    def dataRelease(self): ...

# TODO finish this
class ICPlugin:
    def icDefaultButtonAction(self): ...

    def icDefaultAxialAction(self): ...

    def icEchoDefaultActionTable(self): ...

    def icNewActionMapType(self): ...

    def icActionAllowed(self): ...


class IRCPlugin:
    def ircConnect(self, ircServerAddress, port = None) -> None: ...

    def ircDisconnect(self) -> None: ...

    def ircNick(self, nickname: str) -> None: ...

    def ircName(self, realname: str) -> None: ...

    def ircSend(self, message: str) -> None: ...

    def ircWho(self) -> None: ...

    def ircListChannels(self) -> None: ...

    def ircListPeople(self, channel = None) -> bool: ...

    def ircSetChannel(self, channelName: str) -> bool: ...

    def ircEcho(self, echoType) -> bool: ...


class ESFPlugin:
    def activateObject(self, targetId, fValue: float): ...

    def deactivateObject(self, targetId, fValue: float): ...


# TODO finish this
class ESBasePlugin:
    def initializeServer(self): ...

    def resetPlayerManager(self): ...

    def resetGhostManager(self): ...

    def resetSimTimer(self): ...

    def setPosition(self): ...

    def getPosition(self): ...

    def orbitCamera(self): ...

    def smoothCameraPath(self): ...

    def warpObject(self): ...

    def tagGetString(self): ...

    def forceFrameRender(self): ...

    def newNavigation(self): ...

    def showMem(self): ...

    def purgeDebris(self): ...

    def damage(self): ...

    def damageDetail(self): ...

    def dropPod(self): ...

    def setDropPodParams(self): ...

    def snow(self): ...

    def cycleCamera(self): ...

    def createServer(self): ...

    def checkForDups(self): ...

    def loadExplosionTables(self): ...

    def players(self): ...

    def playerList(self): ...

    def gotoShellRes(self): ...

    def forceToShellRes(self): ...

    def gotoSimRes(self): ...

    def goFullWhenBoth640x480(self): ...

    def getConnectedClient(self): ...

    def ban(self): ...

    def record(self): ...

    def ffEvent(self): ...

    def editWg(self): ...

    def missionEndConditionMet(self): ...

    def notifyMissionEnd(self): ...

    def playerFocusCamera(self): ...

    def focusCamera(self): ...

    def unfocusCamera(self): ...

    def toggleFps(self): ...

    def getKills(self): ...

    def getDeaths(self): ...

    def getPing(self): ...

    def getName(self): ...

    def getMarkerName(self): ...

    def getObjectName(self): ...

    def getObjectId(self): ...

    def getSquad(self): ...

    def getTeam(self): ...

    def getTeamNameForTeamId(self): ...

    def getTeamColorFromBits(self): ...

    def getTeamBitsFromColor(self): ...

    def setTeam(self): ...

    def getTeamAvgPing(self): ...

    def getTeamKills(self): ...

    def getTeamDeaths(self): ...

    def getVehicleHudName(self): ...

    def getHudName(self): ...

    def isShutdown(self): ...

    def isCloaked(self): ...

    def getGroupDistance(self): ...

    def getDistance(self): ...

    def randomInt(self): ...

    def randomFloat(self): ...

    def healObject(self): ...

    def damageObject(self): ...

    def damageArea(self): ...

    def reloadObject(self): ...

    def playSound(self): ...

    def playVoice(self): ...

    def serverInitScoreBoard(self): ...

    def serverResetScores(self): ...

    def messageBox(self): ...

    def localMessageBox(self): ...

    def fadeEvent(self): ...

    def isSafe(self): ...

    def getLeader(self): ...

    class PlayerManager:
        def getPlayerCount(self): ...

        def getPlayer(self): ...

        def getPlayerNum(self): ...

        def vehicleIdToPlayer(self): ...

        def playerNumToVehicle(self): ...

    @property
    def playerManager(self): ...


    def getConnection(self): ...

    def fileWrite(self): ...

    def getDate(self): ...

    def getTime(self): ...

    def getCurrentTime(self): ...

    def getFancyDeathMessage(self): ...

    def strlen(self): ...

    def strAlign(self): ...

    def showVersion(self): ...

    def setHostile(self): ...

    def listHostilities(self): ...

    def TRMissionObjStatus(self): ...

    def loadSinglePlayMission(self): ...

    def convertSpaces(self): ...

    def setHudTimer(self): ...

    def playAnimSequence(self): ...

    def stopAnimSequence(self): ...

    def setAnimSequence(self): ...

    def setNavMarker(self): ...

    def playerDropNavMarker(self): ...

    def isGroupDestroyed(self): ...

    def objectsWithinRadius(self): ...

    def addSquadOrder(self): ...

    def removeSquadOrder(self): ...

    def addGeneralOrder(self): ...

    def removeGeneralOrder(self): ...

    def TRForceToDebrief(self): ...

    def forceToDebrief(self): ...

    def squadVictoryYell(self): ...

    def squawkEnabled(self): ...

    def squawkChatEnabled(self): ...

    def clientCursorOn(self): ...

    def clientCursorOff(self): ...

    def setHudMapViewOffset(self): ...

    def setGameInfo(self): ...

    def joinServer(self): ...

    def copyVolToDisk(self): ...

    def flushVolFromDisk(self): ...

    def loadMissionSoundVolume(self): ...

    def pick(self): ...

    def pickVehicle(self): ...

    def pickStaticShape(self): ...

    def cdAudioNew(self): ...

    def cdAudioCycle(self): ...

    def cdAudoStop(self): ...

    def cdAudioFadeStop(self): ...

    def cdAudioStopOnEndCurTrack(self): ...

    def cdAudioGetVolume(self): ...

    def registerCdAudioTrack(self): ...

    def preLoad(self): ...

    def preLoadFile(self): ...

    def preLoadDts(self): ...

    def preLoadMatrialList(self): ...

    def preLoadExplosionTables(self): ...

    def preLoadEcho(self): ...

    def roundingErrorTest(self): ...

    def fpuShowCw(self): ...

    def fpuSetCw(self): ...

    def isMultiplayer(self): ...

    def setStaticShapeShortName(self): ...

    def setStaticShapeLongName(self): ...

    def lockUserInput(self): ...

    def getVehicleNavMarkerLocation(self): ...

    def getVehicleNavMarkerId(self): ...

    def dist(self): ...

    def setWidescreen(self): ...

    def sethudLabel(self): ...

    def heapCheck(self): ...

    def resetLastHitBy(self): ...

    def getCurrentTargetId(self): ...

    def getShieldDirStr(self): ...

    def stopPlayerVehicle(self): ...

    def flushDustManager(self): ...

    def getCdRomDrive(self): ...

    def checkForFile(self): ...

    def checkDirectXVersion(self): ...

    def checkDisk(self): ...

    def getWindowTitle(self): ...

    def flushConsoleScheduler(self): ...

    def getNavMarkerStatus(self): ...

    def regOk(self): ...

    def regEqual(self): ...

    def setHutChatDisplayType(self): ...

    def createSSMutex(self): ...

    def checkDiskFreeSpace(self): ...

    def appendSearchPath(self): ...

    def isEqualIp(self): ...


# TODO finish this
class ESChatPlugin:
    def say(self): ...

    def say3d(self): ...

    def setChannel(self): ...

    def killChannel(self): ...

    def flushChannel(self): ...

# TODO finish this
class DynamicDataPlugin:
    def dynDataWriteObject(self): ...

    def dynDataReadObject(self): ...

    def dynDataWriteClassType(self): ...

    def dynDataReadClassType(self): ...

    def scanXLoad(self): ...

    def scanXFlush(self): ...

    def scanXEcho(self): ...

    def encyclopediaLoad(self): ...

    def encyclopediaWrite(self): ...

    def encyclopediaFlush(self): ...

    def encyclopediaEcho(self): ...

    def missionBriefLoad(self): ...

    def missionBriefFlush(self): ...

    def missionBriefEcho(self): ...

    def campiagnLoad(self): ...

    def campaignEcho(self): ...

    def gameLoad(self): ...

    def gameSave(self): ...

    def gameSetSquadMate(self): ...

    def gameSetVehicle(self): ...

    def flushPilots(self): ...
